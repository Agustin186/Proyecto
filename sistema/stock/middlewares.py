from django.shortcuts import redirect
from django.urls import reverse
from .models import ArqueoCaja

class CheckOpenCajaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/logout/' and ArqueoCaja.objects.filter(cerrado=False).exists():
            arqueo_abierto = ArqueoCaja.objects.filter(cerrado=False).first()
            return redirect(reverse('cerrar_arqueo', args=[arqueo_abierto.id_caja]))

        response = self.get_response(request)
        return response
