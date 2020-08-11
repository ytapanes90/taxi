from main.models import Cliente, Chofer, Vehiculo, Solicitud, Carrera, Localizacion, Factura, Ranking
from .serializers import ClienteSerializer, ChoferSerializer, VehiculoSerializer, SolicitudSerializer, \
                         CarreraSerializer, LocalizacionSerializer, FacturaSerializer, RankingSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

#Cliente
class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    #permission_classes = (IsAuthenticated,)
    #authentication_class = (TokenAuthentication,)

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

#Chofer
class ChoferList(generics.ListCreateAPIView):
    queryset = Chofer.objects.all()
    serializer_class = ChoferSerializer

class ChoferDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chofer.objects.all()
    serializer_class = ChoferSerializer

#Vehiculo
class VehiculoList(generics.ListCreateAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

class VehiculoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

#Solicitud
class SolicitudList(generics.ListCreateAPIView):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

class SolicitudDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

#Carrera
class CarreraList(generics.ListCreateAPIView):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class CarreraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

#Localizacion
class LocalizacionList(generics.ListCreateAPIView):
    queryset = Localizacion.objects.all()
    serializer_class = LocalizacionSerializer

class LocalizacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Localizacion.objects.all()
    serializer_class = LocalizacionSerializer

#Factura
class FacturaList(generics.ListCreateAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

class FacturaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer

#Ranking
class RankingList(generics.ListCreateAPIView):
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer

class RankingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer


