from django.contrib import admin
from .models import User, Cliente, Chofer, Vehiculo, Solicitud, Carrera, Localizacion, Factura, Ranking

admin.site.register(User)
admin.site.register(Cliente)
admin.site.register(Chofer)
admin.site.register(Vehiculo)
admin.site.register(Solicitud)
admin.site.register(Carrera)
admin.site.register(Localizacion)
admin.site.register(Factura)
admin.site.register(Ranking)


