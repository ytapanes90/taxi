from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password


class User(AbstractUser):
    # id = models.AutoField(primary_key=True)
    # dni = models.CharField(max_length=11)
    # nombre = models.CharField(max_length=100)
    # primer_apellido = models.CharField(max_length=100)
    # segundo_apellido = models.CharField(max_length=100)
    #telefono = models.CharField(max_length=20)
    # correo = models.CharField(max_length=50)

    foto = models.ImageField()
    #distancia_notificacion = models.IntegerField(default=500)

    def __str__(self):
        return '{0} {1}'.format(self.username)

class Cliente(User):
    cantidad_viajes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Cliente, self).save(args,kwargs)


class Chofer(User):
    calificacion = models.DecimalField(default=0, max_digits=2,decimal_places=1)
    activo = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def save(self,*args,**kwargs):
        self.password = make_password(self.password)
        super(Chofer, self).save(args,kwargs)

class Vehiculo(models.Model):
    CONFORT = (
        ('alto', 'Alto'),
        ('medio', 'Medio'),
        ('bajo', 'Bajo'),
    )

    SEGURIDAD = (
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja'),
    )

    TIPO = (
        ('moto', 'Moto'),
        ('carro', 'Carro'),
        ('van', 'Van'),
        ('omnibus', 'Omnibus'),
        ('camion', 'Camion'),
    )

    id = models.AutoField(primary_key=True)
    foto = models.ImageField()
    confort=models.CharField(max_length=20, choices=CONFORT)
    seguridad=models.CharField(max_length=20, choices=SEGURIDAD)
    tipo=models.CharField(max_length=20, choices=TIPO)
    #matricula = models.CharField(max_length=10)
    #marca = models.CharField(max_length=50)
    #modelo = models.CharField(max_length=50)
    #color = models.CharField(max_length=20, choices=COLORS)
    capacidad = models.IntegerField()

    chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE)

    def __str__(self):
        return self.marca +' '+ self.modelo +' '+ self.matricula

class Solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    inicio_latitud = models.DecimalField(max_digits=6,decimal_places=3)
    inicio_longitud = models.DecimalField(max_digits=6,decimal_places=3)
    fin_latitud = models.DecimalField(max_digits=6,decimal_places=3)
    fin_longitud = models.DecimalField(max_digits=6,decimal_places=3)
    descripcion = models.CharField(max_length=255)

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Carrera(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    distancia = models.DecimalField(max_digits=7,decimal_places=2)
    completada = models.BooleanField()

    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE)

class Localizacion(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    latitud = models.DecimalField(max_digits=6,decimal_places=3)
    longitud = models.DecimalField(max_digits=6,decimal_places=3)

    chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE)

class Factura(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.DecimalField(max_digits=10,decimal_places=2)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE)

class Ranking(models.Model):
    posicion = models.IntegerField(primary_key=True)
    puntos = models.IntegerField()

    chofer = models.ForeignKey(Chofer, on_delete=models.CASCADE)



