from main.models import Chofer, Localizacion, Solicitud
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import Utils
from decimal import Decimal
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def notifier(request, room_name):
    id_chofer = room_name.split('_')[1]
    chofer = Chofer.objects.get(id = id_chofer)
    return render(request, 'home.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'chofer': mark_safe(json.dumps(chofer.__str__()))
    })

class Receivers():
    @receiver(post_save, sender=Solicitud)
    def SolicitudPostSave(sender, instance, created, **kwargs):
        if(created):
            localizaciones = Localizacion.objects.filter(chofer__active=True)
            distancia_notificacion_cliente = instance.cliente.distancia_notificacion
            for localizacion in localizaciones:
                distancia = Decimal(Utils.calcularDistancia(instance.inicio_latitud,instance.inicio_longitud,localizacion.latitud,localizacion.longitud))
                distancia_notificacion_chofer = localizacion.chofer.distancia_notificacion
                if distancia <= distancia_notificacion_cliente and distancia <= distancia_notificacion_chofer:
                    print(distancia)
                    print(localizacion.chofer)
                    Utils.sendNotification(instance,localizacion.chofer)