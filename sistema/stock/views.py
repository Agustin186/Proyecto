from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from .forms import EmpleadosForm
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from xhtml2pdf import pisa  ##hacer el pip install xhtml2pdf para que funcione
from .models import *
from .forms import *
from django.utils import timezone
from django.template.loader import get_template
    
def procesar_login(request):    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('inicio')  
        else:
            messages.error(request, "Usuario o contraseña incorrecta")  
    return render(request, "procesar_login.html")


@login_required
def apertura_arqueo(request):
    if request.method == 'POST':
        form = ArqueoCajaForm(request.POST)
        if form.is_valid():
            arqueo = form.save(commit=False)
            arqueo.fecha_hs_apertura = timezone.now()
            arqueo.monto_final = 0
            arqueo.total_ingreso = 0
            arqueo.total_egreso = 0
            arqueo.save()
            return redirect('historial_arqueo')
    else:
        form = ArqueoCajaForm()
    return render(request, 'caja/apertura_arqueo.html', {'form': form})


def cerrar_arqueo(request, id_caja):
    arqueo = get_object_or_404(ArqueoCaja, id_caja=id_caja)

    if request.method == 'POST':
        form = CerrarArqueoForm(request.POST, instance=arqueo)
        if form.is_valid():
            # Al cerrar la caja, calcular el monto final
            arqueo.cerrar_caja()
            return redirect('historial_arqueo')
    else:
        form = CerrarArqueoForm(instance=arqueo)

    return render(request, 'caja/cerrar_arqueo.html', {'form': form, 'arqueo': arqueo})


def historial_arqueo(request):
    arqueos = ArqueoCaja.objects.all()

    # Recalcular montos para todos los arqueos (opcional)
    for arqueo in arqueos:
        arqueo.calcular_montos()

    return render(request, 'caja/historial_arqueo.html', {'arqueos': arqueos})

@login_required
def inicio(request):
    producto=Productos.objects.all()
    return render (request, "inicio.html",{"productos":producto})




def cerrar_sesion(request):
    if ArqueoCaja.objects.filter(cerrado=False).exists():
        arqueo_abierto = get_object_or_404(ArqueoCaja, cerrado=False)
        return redirect('cerrar_arqueo', id_caja=arqueo_abierto.id_caja)

    logout(request)
    return redirect('procesar_login')



##CRUD Articulos
def mostrar_articulos(request):
    producto=Productos.objects.all()
    return render(request, "articulos/mostrar.html",{"productos":producto})

@permission_required('stock.view_articulo')
def editar_articulos(request,id_prod):
    producto = Productos.objects.get(id_prod=id_prod)
    formulario = ProductosForm(request.POST or None, request.FILES or None, instance=producto)

    if request.method == 'POST':
        if formulario.is_valid():  
            formulario.save()  
            messages.success(request, "Artículo editado exitosamente.")  
            return redirect('mostrar_articulos') 

    return render(request, "articulos/editar.html", {"formulario": formulario})

def crear_articulos(request):
    formulario = ProductosForm(request.POST or None)
    if request.method == 'POST':  # 
        if formulario.is_valid():
            formulario.save()
            return redirect("mostrar_articulos")
    return render(request, "articulos/crear.html", {"formulario": formulario})


@permission_required('stock.view_articulo')
def eliminar_productos(request,id_prod):
    producto = Productos.objects.get(id_prod=id_prod)
    producto.delete()
    return redirect("mostrar_articulos")
##CRUD Clientes
def mostrar_clientes(request):
    cliente=Clientes.objects.all()
    return render(request, "clientes/mostrar.html",{"clientes":cliente})

@permission_required('stock.view_cliente')
def editar_clientes(request, id_cli):
    cliente = Clientes.objects.get(id_cli=id_cli)
    formulario = ClientesForm(request.POST or None, request.FILES or None, instance=cliente)
    
    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Cliente editado exitosamente.")
            return redirect('mostrar_clientes') 

    return render(request, "clientes/editar.html", {"formulario": formulario})


@permission_required('stock.view_cliente')
def crear_clientes(request):
    formulario = ClientesForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("mostrar_clientes")
    return render(request,"clientes/crear.html",{"formulario": formulario})
##Borrar_clientes
@permission_required('stock.view_cliente')
def eliminar_clientes(request, id_cli):
    cliente = Clientes.objects.get(id_cli=id_cli)
    cliente.delete()
    return redirect("mostrar_clientes")


##CRUD Empleados
def mostrar_empleados(request):
    empleado=Empleados.objects.all()
    return render(request,"empleados/mostrar.html",{"empleados":empleado})

@permission_required('stock.view_empleado')
def editar_empleados(request, id_emplead):
    # Obtener el empleado o devolver 404 si no existe
    empleado = get_object_or_404(Empleados, id_emplead=id_emplead)
    
    # Crear el formulario con los datos existentes del empleado
    formulario = EmpleadosForm(request.POST or None, request.FILES or None, instance=empleado)

    # Si el formulario es válido, guardamos los cambios
    if formulario.is_valid():
        formulario.save()  # Guarda los cambios del empleado en la base de datos
        messages.success(request, 'Datos personales del empleado actualizados correctamente.')
        return redirect('mostrar_empleados')  # Redirigir a la lista de empleados

    # Renderizamos la página de edición si es GET o el formulario no es válido
    return render(request, "empleados/editar.html", {"formulario": formulario, "empleado": empleado})




@permission_required('stock.view_empleado')
def crear_empleados(request):
    formulario = EmpleadosForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect("mostrar_empleados")
    return render(request, "empleados/crear.html",{"formulario": formulario})

@permission_required('stock.view_empleado')
def eliminar_empleados(request, id_emplead):
    empleado = Empleados.objects.get(id_emplead=id_emplead)
    empleado.delete()
    messages.success(request, "Empleado y usuario eliminados correctamente.")
    return redirect("mostrar_empleados")

##CRUD Proveedores
def mostrar_proveedores(request):
    proveedor= Proveedores.objects.all()
    return render(request, "proveedores/mostrar.html",{"proveedores": proveedor})

@permission_required('stock.view_empleado')
def editar_proveedores(request, id_prov):
   
    proveedor = get_object_or_404(Proveedores, id_prov=id_prov)
    

    formulario = ProveedoresForm(request.POST or None, request.FILES or None, instance=proveedor)

    if formulario.is_valid():
        formulario.save()  
        messages.success(request, 'Proveedor actualizado correctamente.')
        return redirect('mostrar_proveedores')  
    
   
    return render(request, "proveedores/editar.html", {"formulario": formulario})

@permission_required('stock.view_empleado')
def crear_proveedores(request):
    formulario = ProveedoresForm(request.POST or None)
    if formulario.is_valid ():
     formulario.save()
     return redirect("mostrar_proveedores")
    return render(request, "proveedores/crear.html", {"formulario": formulario})

@permission_required('stock.view_empleado')
def eliminar_proveedores(request,id_prov):
    proveedor = Proveedores.objects.get(id_prov=id_prov)
    proveedor.delete()
    return redirect("mostrar_proveedores")

##Compras
def mostrar_compras(request):
    return render(request,"compras/crear_compra.html")




def crear_venta(request):
    producto = Productos.objects.all()
    empleado = Empleados.objects.all()
    cliente = Clientes.objects.all()

    arqueo_abierto = ArqueoCaja.objects.filter(cerrado=False).first()  # Buscar el arqueo abierto
    
    if not arqueo_abierto:
        # Si no hay arqueo abierto, redirigir con mensaje
        return redirect('historial_arqueo')

    if request.method == "POST":
        id_cli = request.POST.get('cliente')    
        total_venta = request.POST.get('total') 

        nueva_venta = Ventas(
            id_caja=arqueo_abierto,  # Asociar venta al arqueo de caja abierto
            id_cli=Clientes.objects.get(id_cli=id_cli),  
            total_venta=total_venta,
            fecha_hs=timezone.now()
        )
        nueva_venta.save()

        productos_ids = request.POST.getlist('productos[]')
        cantidades = request.POST.getlist('cantidades[]')
        subtotales = request.POST.getlist('subtotales[]')

        for i in range(len(productos_ids)):
            producto = Productos.objects.get(id_prod=productos_ids[i])
            cantidad = int(cantidades[i])
            subtotal = float(subtotales[i])

            nuevo_detalle = det_ventas(
                id_prod=producto,
                id_venta=nueva_venta,
                precio_prod=producto.precio_prod,
                subtotal_venta=subtotal,
                cant_vendida=cantidad
            )
            nuevo_detalle.save()

            producto.stock_actual -= cantidad
            producto.save()

        # Registrar automáticamente el ingreso en el arqueo de caja
        nuevo_ingreso = Ingreso(
            id_caja=arqueo_abierto,
            descripcion=f"Venta {nueva_venta.id_venta}",
            monto=total_venta
        )
        nuevo_ingreso.save()

        # Actualizar los montos en el arqueo de caja
        arqueo_abierto.calcular_montos()

        return redirect('det_venta', id_venta=nueva_venta.id_venta)

    else:
        formulario = VentasForm()

    context = {
        "empleados": empleado,
        "clientes": cliente,
        "productos": producto,
        "formulario": formulario
    }

    return render(request, "ventas/crear_venta.html", context)




def det_venta(request, id_venta):
    venta = get_object_or_404(Ventas, id_venta=id_venta)
    detalles = det_ventas.objects.filter(id_venta=venta)

    context = {
        'venta': venta,
        'detalles': detalles
    }

    return render(request, 'ventas/detalle_ventas.html', context)


def GenerarPdf(request,id_venta ):
    venta=Ventas.objects.get(id_venta=id_venta)
    detalles=det_ventas.objects.filter(id_venta=venta)

    context={
        "venta":venta,
        "detalles":detalles,
    }
    template =get_template("ventas/detalle_ventas_pdf.html")
    html=template.render(context)
    
    response=HttpResponse(content_type="aplication/pdf")
    response["content-disposition"]=f'attachment; filename="DetalleVenta_{venta.id_venta}.pdf"'

    pisa_status= pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse(f"error: {pisa_status.err}")
    return response

def historial_ventas(request):
    ventas=Ventas.objects.all().order_by("-fecha_hs")
    context={
        "ventas": ventas
    }

    return render (request, "ventas/historial_ventas.html", context)






from django.shortcuts import get_object_or_404
from .models import ArqueoCaja, Ingreso, Egreso

def registrar_ingreso(request):
    arqueo_abierto = ArqueoCaja.objects.filter(cerrado=False).first()
    if not arqueo_abierto:
        # Si no hay ninguna caja abierta, redirigir con un mensaje
        return redirect('historial_arqueo')

    if request.method == 'POST':
        form = IngresoForm(request.POST)
        if form.is_valid():
            ingreso = form.save(commit=False)
            ingreso.id_caja = arqueo_abierto
            ingreso.save()
            return redirect('historial_arqueo')
    else:
        form = IngresoForm(initial={'id_caja': arqueo_abierto})
    return render(request, 'transacciones/registrar_ingreso.html', {'form': form, 'arqueo_abierto': arqueo_abierto})


def registrar_egreso(request):
    arqueo_abierto = ArqueoCaja.objects.filter(cerrado=False).first()
    if not arqueo_abierto:
        return redirect('historial_arqueo')

    if request.method == 'POST':
        form = EgresoForm(request.POST)
        if form.is_valid():
            egreso = form.save(commit=False)
            egreso.id_caja = arqueo_abierto
            egreso.save()
            arqueo_abierto.calcular_montos()  # Recalcula los montos cada vez que se registra un egreso
            return redirect('historial_arqueo')
    else:
        form = EgresoForm()
    return render(request, 'transacciones/registrar_egreso.html', {'form': form, 'arqueo_abierto': arqueo_abierto})
