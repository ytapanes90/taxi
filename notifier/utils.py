from math import sin, cos, acos
from decimal import Decimal
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

class Utils():
    def calcularDistancia(long1,lat1,long2,lat2):
        degtorad = 0.01745329
        radtodeg = 57.29577951

        dlong = (long1 - long2)
        dvalue = (sin(lat1 * Decimal(degtorad)) * sin(lat2 * Decimal(degtorad))) + (cos(lat1 * Decimal(degtorad)) *cos(lat2 * Decimal(degtorad))*cos(dlong * Decimal(degtorad)))

        dd = acos(dvalue) * radtodeg

        miles = (dd * 69.16)
        km = (dd * 111.302)

        return km

    def sendNotification(solicitud, chofer):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "chofer_"+str(chofer.id),{
                "type": "notification",
                "message": {
                    "cliente": str(solicitud.cliente),
                    "solicitud": solicitud.id,
                    "inicio_latitud": str(solicitud.inicio_latitud),
                    "inicio_longitud": str(solicitud.inicio_longitud),
                    "fin_latitud": str(solicitud.fin_latitud),
                    "fin_longitud": str(solicitud.fin_longitud)
                }
            }
        )