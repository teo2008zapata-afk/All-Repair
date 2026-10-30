from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render
from .models import Repuesto, Servicio


def inicio(request):
    return render(request, 'allrepair/public/index.html')


def nosotros(request):
    return render(request, 'allrepair/public/nosotros.html')


def catalogo(request):
    return render(request, 'allrepair/public/catalogo.html')


def servicios(request):
    return render(request, 'allrepair/public/servicios.html')


def blog(request):
    return render(request, 'allrepair/public/blog.html')


def contactanos(request):
    return render(request, 'allrepair/public/contactanos.html')


# -------------------- REPUESTOS --------------------
def crear(request):
    if request.method == 'POST':
        Repuesto.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            precio=request.POST['precio'],
            stock=request.POST['stock'],
        )
    return render(request, 'allrepair/repuestos/formulario.html')


def listar(request):
    repuestos = Repuesto.objects.all()
    return render(request, 'allrepair/repuestos/lista.html', {'repuestos': repuestos})


def detalle(request, id):
    repuesto = Repuesto.objects.get(id=id)
    return render(request, 'allrepair/repuestos/detalle.html', {'Repuesto': repuesto})


def editar(request, id):
    repuesto = Repuesto.objects.get(id=id)
    if request.method == 'POST':
        repuesto.nombre = request.POST['nombre']
        repuesto.descripcion = request.POST['descripcion']
        repuesto.precio = request.POST['precio']
        repuesto.stock = request.POST['stock']
        repuesto.save()
        return render(request, 'allrepair/repuestos/detalle.html', {'Repuesto': repuesto})
    return render(request, 'allrepair/repuestos/formulario.html', {'Repuesto': repuesto})


def eliminar(request, id):
    repuesto = Repuesto.objects.get(id=id)
    repuesto.delete()
    return redirect('repuesto_lista')


# -------------------- SERVICIOS --------------------
def crear_servicio(request):
    if request.method == 'POST':
        Servicio.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion'],
            precio=request.POST['precio'],
        )
    return render(request, 'allrepair/servicios/formulario1.html')


def listar_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'allrepair/servicios/lista1.html', {'servicios': servicios})


def detalle_servicio(request, id):
    servicio = Servicio.objects.get(id=id)
    return render(request, 'allrepair/servicios/detalle1.html', {'Servicio': servicio})


def editar_servicio(request, id):
    servicio = Servicio.objects.get(id=id)
    if request.method == 'POST':
        servicio.nombre = request.POST['nombre']
        servicio.descripcion = request.POST['descripcion']
        servicio.precio = request.POST['precio']
        servicio.save()
        return render(request, 'allrepair/servicios/detalle1.html', {'Servicio': servicio})
    return render(request, 'allrepair/servicios/formulario1.html', {'Servicio': servicio})


def eliminar_servicio(request, id):
    servicio = Servicio.objects.get(id=id)
    servicio.delete()
    return redirect('servicio_lista')


# -------------------- AUTENTICACION DEL ADMINISTRADOR --------------------
def es_administrador(user):
    return user.is_authenticated and (user.is_superuser or user.is_staff)


def iniciar_sesion(request):
    if request.user.is_authenticated and es_administrador(request.user):
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)

        if user is not None and (user.is_superuser or user.is_staff):
            login(request, user)
            return redirect(request.GET.get('next', '/administrador/'))

        return render(request, 'allrepair/usuarios/login.html', {
            'error': 'Las credenciales son incorrectas o el usuario no tiene permisos de administrador.'
        })

    return render(request, 'allrepair/usuarios/login.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('login')


# -------------------- DASHBOARD PERSONALIZADO --------------------
@login_required(login_url='/administrador/login/')
@user_passes_test(es_administrador, login_url='/administrador/login/')
def dashboard(request):
    return render(request, 'allrepair/admin/dashboard.html', {
        'total_repuestos': Repuesto.objects.count(),
        'total_servicios': Servicio.objects.count(),
    })
