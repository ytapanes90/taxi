from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^v1/cliente/$', views.ClienteList.as_view()),
    url(r'^v1/cliente/(?P<pk>[0-9]+)/$', views.ClienteDetail.as_view()),
    url(r'^v1/chofer/$', views.ChoferList.as_view()),
    url(r'^v1/chofer/(?P<pk>[0-9]+)/$', views.ChoferDetail.as_view()),
    url(r'^v1/vehiculo/$', views.VehiculoList.as_view()),
    url(r'^v1/vehiculo/(?P<pk>[0-9]+)/$', views.VehiculoDetail.as_view()),
    url(r'^v1/solicitud/$', views.SolicitudList.as_view()),
    url(r'^v1/solicitud/(?P<pk>[0-9]+)/$', views.SolicitudDetail.as_view()),
    url(r'^v1/carrera/$', views.CarreraList.as_view()),
    url(r'^v1/carrera/(?P<pk>[0-9]+)/$', views.CarreraDetail.as_view()),
    url(r'^v1/localizacion/$', views.LocalizacionList.as_view()),
    url(r'^v1/localizacion/(?P<pk>[0-9]+)/$', views.LocalizacionDetail.as_view()),
    url(r'^v1/factura/$', views.FacturaList.as_view()),
    url(r'^v1/factura/(?P<pk>[0-9]+)/$', views.FacturaDetail.as_view()),
    url(r'^v1/ranking/$', views.RankingList.as_view()),
    url(r'^v1/ranking/(?P<pk>[0-9]+)/$', views.RankingDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

