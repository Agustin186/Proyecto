from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Empleados

#Proveedores
from .models import Proveedores
admin.site.register(Proveedores)
#Clientes
from .models import Clientes
admin.site.register(Clientes)

#Empleados


#Productos
from .models import Productos
admin.site.register(Productos)



class EmpleadosInline(admin.StackedInline):
    model = Empleados
    can_delete = False
    verbose_name_plural = 'Empleados'

class UserAdmin(BaseUserAdmin):
    inlines = (EmpleadosInline,)

# Desregistrar el UserAdmin original
admin.site.unregister(User)
# Registrar el nuevo UserAdmin
admin.site.register(User, UserAdmin)