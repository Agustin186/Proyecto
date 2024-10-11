from django import forms
from .models import *
from django.contrib.auth.models import User

class ProveedoresForm(forms.ModelForm):
    class Meta:
        model = Proveedores
        fields = "__all__"

class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields="__all__"

class EmpleadosForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=False)  # No requerido al editar
    password = forms.CharField(widget=forms.PasswordInput, required=False)  # No requerido al editar

    class Meta:
        model = Empleados
        fields = ['nombre_emplead', 'apellido_emplead', 'dni_emplead', 'direcc_emplead',
                'tel_emplead', 'correo_emplead', 'sueldo_emplead', 'fecha_inicio', 'fecha_fin']

    def save(self, commit=True):
        empleado = super().save(commit=False)
        
        # Si estamos creando un nuevo empleado, creamos el usuario
        if not empleado.user:
            user = User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password'],
                email=self.cleaned_data['correo_emplead']
            )
            empleado.user = user
        else:
            # Si estamos editando un empleado, actualizamos el usuario solo si hay cambios
            user = empleado.user
            if self.cleaned_data['username']:
                user.username = self.cleaned_data['username']
            if self.cleaned_data['password']:
                user.set_password(self.cleaned_data['password'])
            user.save()

        if commit:
            empleado.save()
        return empleado


    def save(self, commit=True):
        empleado = super().save(commit=False)

        if self.cleaned_data.get('username'):
            if self.instance.user:
                user = self.instance.user  # Update existing user
                user.username = self.cleaned_data['username']
                if self.cleaned_data['password']:
                    user.set_password(self.cleaned_data['password'])  # Update password only if provided
            else:
                # Create a new user if one doesn't exist
                user = User.objects.create_user(
                    username=self.cleaned_data['username'],
                    password=self.cleaned_data['password'],
                    email=self.cleaned_data['correo_emplead']
                )
            user.save()
            empleado.user = user

        if commit:
            empleado.save()
        return empleado


from django import forms
from .models import Productos  # Asegúrate de que la ruta sea correcta

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre_prod', 'precio_prod', 'stock_min', 'stock_max', 'stock_actual', 'punto_reposicion'] 

    def clean_nombre_prod(self):
        nombre_prod = self.cleaned_data.get('nombre_prod')
        if not nombre_prod:
            raise forms.ValidationError("El nombre del artículo es obligatorio.")
        return nombre_prod

    def clean_precio_prod(self):
        precio_prod = self.cleaned_data.get('precio_prod')
        if precio_prod is None or precio_prod < 0:
            raise forms.ValidationError("El precio debe ser un número positivo.")
        return precio_prod

    def clean_stock_min(self):
        stock_min = self.cleaned_data.get('stock_min')
        if stock_min is not None and stock_min < 0:
            raise forms.ValidationError("El stock mínimo no puede ser negativo.")
        return stock_min


    def clean_stock_max(self):
        stock_max = self.cleaned_data.get('stock_max')
        if stock_max is not None and stock_max < 0:
            raise forms.ValidationError("El stock máximo no puede ser negativo.")
        return stock_max

    def clean_stock_actual(self):
        stock_actual = self.cleaned_data.get('stock_actual')
        if stock_actual is not None and stock_actual < 0:
            raise forms.ValidationError("El stock actual no puede ser negativo.")
        return stock_actual

    def clean_punto_reposicion(self):
        punto_reposicion = self.cleaned_data.get('punto_reposicion')
        if punto_reposicion is not None and punto_reposicion < 0:
            raise forms.ValidationError("El punto de reposición no puede ser negativo.")
        return punto_reposicion

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields=["id_caja","id_cli", "total_venta", "fecha_hs"]

class ArqueoCajaForm(forms.ModelForm):
    class Meta:
        model = ArqueoCaja
        fields = ['id_emplead', 'monto_inicial']


class CerrarArqueoForm(forms.ModelForm):
    class Meta:
        model = ArqueoCaja
        fields = []
        



class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ['descripcion', 'monto']

class EgresoForm(forms.ModelForm):
    class Meta:
        model = Egreso
        fields = ['descripcion', 'monto']

