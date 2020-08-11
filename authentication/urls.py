from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken'))
]

