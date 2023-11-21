from django.shortcuts import render, redirect
from django.contrib import messages
from app.forms import *
from app.models import *


def index(request):
    sesion = request.session
   
    if "administrador" in sesion:
        return redirect('administrador')
    else:
        return render(request, "index.html")


def listaUsuarios(request):
    print("lista")
    listaUsuarios = Usuario.objects.all()
    return render(request, "listaUsuarios.html", {"usuarios": listaUsuarios})

def listaPlanesInternet(request):
    listaPlanesInternet = Plan_Internet.objects.all()
    return render(request, "listaPlanesInternet.html", {"planesInternet": listaPlanesInternet})

def listaPlanesTelefonia(request):
    listaPlanesTelefonia = Plan_Telefonia.objects.all()
    return render(request, "listaPlanesTelefonia.html", {"planesTelefonia": listaPlanesTelefonia})

def listaPlanesTelevision(request):
    listaPlanesTelevision = Plan_Television.objects.all()
    return render(request, "listaPlanesTelevision.html", {"planesTelevision": listaPlanesTelevision})

def editar_plan_internet(request):
    planInternet = Plan_Internet.objects.get(id=id)
    if request.method == 'GET':
        formulario = FormPlanInternet(instance=planInternet)

        return render(request, 'editar_plan_internet.html',  {"form":formulario, "id": id})
    elif request.method == 'POST':
        formulario = FormPlanInternet(request.POST, instance=planInternet)
        if formulario.is_valid():
            formulario.save()
        return redirect('listaPlanesInternet')
    return render(request, 'editar_plan_internet.html')

def editar_plan_television(request):
    planTelevision = Plan_Television.objects.get(id=id)
    if request.method == 'GET':
        formulario = FormPlanTelevision(instance=planTelevision)

        return render(request, 'editar_plan_television.html',  {"form":formulario, "id": id})
    elif request.method == 'POST':
        formulario = FormPlanTelevision(request.POST, instance=planTelevision)
        if formulario.is_valid():
            formulario.save()
        return redirect('listaPlanesTelevision')
    return render(request, 'editar_plan_television.html')

def editar_plan_telefonia(request):
    planTelefonia = Plan_Telefonia.objects.get(id=id)
    if request.method == 'GET':
        formulario = FormPlanTelefonia(instance=planTelefonia)

        return render(request, 'editar_plan_telefonia.html',  {"form":formulario, "id": id})
    elif request.method == 'POST':
        formulario = FormPlanTelefonia(request.POST, instance=planTelefonia)
        if formulario.is_valid():
            formulario.save()
        return redirect('listaPlanesTelefonia')
    return render(request, 'editar_plan_telefonia.html')

def editarUsuarios(request,id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'GET':
        formulario = FormUsuario(instance=usuario)

        return render(request, 'editarUsuarios.html',  {"form":formulario, "id": id})
    elif request.method == 'POST':
        formulario = FormUsuario(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
        return redirect('listaUsuarios')

def eliminarUsuarios(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    listaUsuarios = Usuario.objects.all()
    return render(request, 'listaUsuarios.html', {"usuarios": listaUsuarios})

def eliminarPlanInternet(request, id):
    planInternet = Plan_Internet.objects.get(id=id)
    planInternet.delete()
    listaPlanesInternet = Plan_Internet.objects.all()
    return render(request, 'listaPlanesInternet.html', {"listaPlanesInternet": listaPlanesInternet})

def eliminarTelefonia(request, id):
    planTelefonia = Plan_Telefonia.objects.get(id=id)
    planTelefonia.delete()
    listaPlanesTelefonia = Plan_Telefonia.objects.all()
    return render(request, 'listaPlanesTelefonia.html', {"listaPlanesTelefonia": listaPlanesTelefonia})

def eliminarTelevision(request, id):
    planTelevision = Plan_Television.objects.get(id=id)
    planTelevision.delete()
    listaPlanesTelevision = Plan_Television.objects.all()
    return render(request, 'listaPlanesTelevision.html', {"listaPlanesTelevision": listaPlanesTelevision})

def cerrar_sesion(request):
    sesion = request.session
    try:
        if "username" in sesion:
            del sesion["username"]
            del sesion["planes"]
        elif "administrador" in sesion:
            del sesion["administrador"]
        return redirect('inicioSesion')
    except:
        return redirect('inicioSesion')
    
def es_administrador(user):
    return user.is_authenticated and user.tipo_usuario.nombre == 'Administrador'

def administrador(request):
    return render(request, "administrador.html", {"username": request.session["administrador"]})

def editar_perfil(request):
    return render(request, 'editar_perfil.html')

def planes_telefonia(request):
    return render(request, "planes_telefonia.html")

def planes_television(request):
    return render(request, 'planes_television.html')

def planS(request):
    return render(request, "planS.html")

def planM(request):
    return render(request, "planM.html")

def planL(request):
    return render(request, "planL.html")

def planXL(request):
    return render(request, "planXL.html")

def cliente_dashboard(request):
    return render(request, "cliente_dashboard.html")

def admin_dashboard(request):
    return render(request, "admin_dashboard.html")

def empleado_dashboard(request):
    return render(request, "empleado_dashboard.html")

def enviar_comentario(request):
    return render(request, "enviar_comentario.html")

def registro(request):
    if request.method == "GET":
        return render(request, "registroUsuario.html")
    elif request.method == "POST":
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        numero = request.POST.get('numero')
        comuna = request.POST.get('comuna')
        direccion = request.POST.get('direccion')
        contrasena = request.POST.get('contrasena')
        nuevoRegistro = Usuario(rut=rut,
                          nombre=nombre,
                          apellido=apellido,
                          correo=correo,
                          numero=numero,
                          comuna=comuna,
                          direccion=direccion,
                          contrasena=contrasena,
                          rol_id=1)
        
        if nuevoRegistro:
            nuevoRegistro.save()
            messages.success(request, 'Registro exitoso. Por favor, inicia sesión.')
            return redirect('inicio_sesion')
        else:
            messages.error(request, 'Error en el formulario. Verifica los datos ingresados.')
            return render(request, 'registro_usuario.html', {"error": 'Error en el formulario. Verifica los datos ingresados.'})

        

def login_view(request):
    if request.method == "GET":
        return render(request, "inicioSesion.html")
    elif request.method == "POST":
        getUsuario = request.POST.get('rut')
        getContrasena = request.POST.get('contrasena')
        usuario = Usuario.objects.filter(rut=getUsuario, 
                                         contrasena=getContrasena).first()

        if usuario and usuario.rol_id==1:
            # Para agregar un valor dentro de la SESSION, lo hacemos como si fuera un diccionario
            request.session["cliente"] = getUsuario
            print(f"El usuario {getUsuario} ha iniciado sesión.")
            return render(request, "index.html", {'rut':getUsuario})
        
        elif usuario and usuario.rol_id==2:
            # Para agregar un valor dentro de la SESSION, lo hacemos como si fuera un diccionario
            request.session["empleado"] = getUsuario
            print(f"El usuario {getUsuario} ha iniciado sesión.")
            return render('empleado_dashboard.html',{'rut':getUsuario})
        
        elif usuario and usuario.rol_id==3:
            request.session["administrador"] = getUsuario
            print(f"El usuario {getUsuario} ha iniciado sesión.")
            return render(request, 'admin_dashboard.html',{'rut':getUsuario})
        
        else:
            error_message = "Por favor, ingrese un nombre de usuario."
            return render(request, "inicioSesion.html", {"error_message": error_message})


def resumen_plan_internet(request, plan_id):
    plan = Plan_Internet.objects.get(id=plan_id)
    return render(request, 'resumen_plan_internet.html', {'plan': plan})

def resumen_plan_television(request, plan_id):
    plan = Plan_Television.objects.get(id=plan_id)
    return render(request, 'resumen_plan_television.html', {'plan': plan})

def resumen_plan_telefonia(request, plan_id):
    plan = Plan_Telefonia.objects.get(id=plan_id)
    return render(request, 'resumen_plan_telefonia.html', {'plan': plan})

def confirmar_suscripcion(request):
    # Aquí iría la lógica para procesar la suscripción, pero necesito el login para que los datos del clinete y el plan se puedan insertar en base de datos.
    return render(request, 'confirmar_suscripcion.html')

def planes_internet(request):
    return render(request, 'planes_internet.html')


def formUsuario(request):
    if request.method == "GET":
        form = FormUsuario()
        return render(request, 'agregarUsuario.html', {"form": form})
    elif request.method == "POST":
        form = FormUsuario(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'agregarUsuario.html', {"form": form})

def formPlanInternet(request):
    if request.method == "GET":
        form = FormPlanInternet()
        return render(request, 'agregarPlanInternet.html', {"form": form})
    elif request.method == "POST":
        form = FormPlanInternet(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'agregarPlanInternet.html', {"form": form})

def formPlanTelevision(request):
    if request.method == "GET":
        form = FormPlanTelevision()
        return render(request, 'agregarPlanTelevision.html', {"form": form})
    elif request.method == "POST":
        form = FormPlanTelevision(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'agregarPlanTelevision.html', {"form": form})

def formPlanTelefonia(request):
    if request.method == "GET":
        form = FormPlanTelefonia()
        return render(request, 'agregarPlanTelefonia.html', {"form": form})
    elif request.method == "POST":
        form = FormPlanTelefonia(request.POST)
        
        if form.is_valid():
            form.save()
        return render(request, 'agregarPlanTelefonia.html', {"form": form})