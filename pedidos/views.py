from django.shortcuts import render, get_object_or_404, redirect
from .models import Pedido, Seguimiento
from .forms import PedidoForm, SeguimientoForm
from uuid import uuid4
from django.contrib.auth.decorators import login_required
from functools import wraps
from django.contrib import messages
from django.utils import timezone
from .utils import siguiente_estado, estado_anterior


def group_required(group_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.groups.filter(name=group_name).exists():
                return redirect('lista_pedidos')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


@login_required
def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos/lista_pedidos.html', {'pedidos': pedidos})


@login_required
def detalle_pedido(request, codigo):
    pedido = get_object_or_404(Pedido, codigo=codigo)
    seguimientos = pedido.seguimientos.all()
    return render(request, 'pedidos/detalle_pedidos.html', {
        'pedido': pedido,
        'seguimientos': seguimientos
    })


@login_required
def crear_pedido(request):
    user = request.user
    if not (user.groups.filter(name='Diseñador').exists() or user.groups.filter(name='Administrador').exists()):
        messages.error(request, "No tienes permiso para crear pedidos.")
        return redirect('lista_pedidos')

    if request.method == 'POST':
        form = PedidoForm(request.POST, request.FILES)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.codigo = f"P{uuid4().hex[:8].upper()}"
            pedido.creado_por = user
            pedido.estado = 'diseñador'
            pedido.save()
            messages.success(request, "Pedido creado correctamente.")
            return redirect('detalle_pedido', codigo=pedido.codigo)
    else:
        form = PedidoForm()

    return render(request, 'pedidos/crear_pedidos.html', {'form': form})


@login_required
def agregar_seguimiento(request, codigo):
    pedido = get_object_or_404(Pedido, codigo=codigo)

    if request.method == 'POST':
        form = SeguimientoForm(request.POST)
        if form.is_valid():
            seguimiento = form.save(commit=False)
            seguimiento.pedido = pedido
            seguimiento.creado_por = request.user  # Si el modelo Seguimiento lo tiene
            seguimiento.save()

            pedido.actualizado_por = request.user
            pedido.actualizado_en = timezone.now()
            pedido.save()

            return redirect('detalle_pedidos', codigo=codigo)
    else:
        form = SeguimientoForm()

    return render(request, 'pedidos/agregar_seguimiento.html', {'form': form, 'pedido': pedido})


@login_required
def dashboard(request):
    user = request.user
    if user.groups.filter(name='Administrador').exists():
        pedidos = Pedido.objects.all()
    elif user.groups.filter(name='Diseñador').exists():
        pedidos = Pedido.objects.filter(estado='diseñador')
    elif user.groups.filter(name='Impresor').exists():
        pedidos = Pedido.objects.filter(estado='impresor')
    elif user.groups.filter(name='Entelador').exists():
        pedidos = Pedido.objects.filter(estado='entelador')
    elif user.groups.filter(name='Embolsador').exists():
        pedidos = Pedido.objects.filter(estado='embolsador')
    else:
        pedidos = Pedido.objects.none()
    return render(request, 'pedidos/dashboard.html', {'pedidos': pedidos})


@login_required
def procesar_pedido(request, codigo):
    pedido = get_object_or_404(Pedido, codigo=codigo)
    user = request.user

    grupo = None
    if user.groups.filter(name='Diseñador').exists():
        grupo = 'diseñador'
    elif user.groups.filter(name='Impresor').exists():
        grupo = 'impresor'
    elif user.groups.filter(name='Entelador').exists():
        grupo = 'entelador'
    elif user.groups.filter(name='Embolsador').exists():
        grupo = 'embolsador'
    else:
        return redirect('dashboard')

    if pedido.estado != grupo:
        return redirect('dashboard')

    if request.method == 'POST':
        accion = request.POST.get('accion')
        observacion = request.POST.get('observacion', '')

        if accion == 'aprobar':
            pedido.estado = siguiente_estado(pedido.estado)
            pedido.observacion = ''
        elif accion == 'devolver':
            pedido.estado = estado_anterior(pedido.estado)
            pedido.observacion = observacion

        pedido.actualizado_por = user
        pedido.actualizado_en = timezone.now()
        pedido.save()

        return redirect('dashboard')

    return render(request, 'pedidos/procesar_pedidos.html', {'pedido': pedido})


@login_required
@group_required('Administrador')
def vista_administradores(request):
    return render(request, 'pedidos/vista_administradores.html')


@login_required
@group_required('Diseñador')
def vista_designers(request):
    return render(request, 'pedidos/vista_designers.html')


@login_required
@group_required('Entelador')
def vista_enteladores(request):
    return render(request, 'pedidos/vista_enteladores.html')


@login_required
@group_required('Impresor')
def vista_impresores(request):
    return render(request, 'pedidos/vista_impresores.html')


@login_required
@group_required('Embolsador')
def vista_embolsadores(request):
    return render(request, 'pedidos/vista_embolsadores.html')
