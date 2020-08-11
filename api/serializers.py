from rest_framework import serializers
from main.models import Cliente, Chofer, Vehiculo, Solicitud, Carrera, Localizacion, Factura, Ranking


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'username', 'password', 'foto', 'cantidad_viajes')

class ChoferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chofer
        fields = ('id', 'username', 'password', 'foto', 'calificacion', 'activo')

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ('id', 'foto', 'confort', 'seguridad', 'tipo', 'capacidad', 'chofer')

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ('id','fecha', 'inicio_latitud', 'inicio_longitud', 'fin_latitud', 'fin_longitud', 'descripcion', 'cliente')

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = ('id','fecha', 'distancia', 'completada', 'solicitud', 'chofer')

class LocalizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacion
        fields = ('id','fecha', 'latitud', 'longitud', 'chofer')

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = ('id','cantidad', 'fecha_actualizacion', 'chofer')

class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = ('id','posicion', 'puntos', 'chofer')