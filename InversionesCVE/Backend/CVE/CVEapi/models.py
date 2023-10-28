from django.db import models

# Create your models here.


TIPO_ESTADO = {
    ("P","Pendiente"),
    ("A","Activo")
}

TIPO_CONTRATO = {
    ("Vi","Vigente"),
    ("Ve","Vencido")
}


class Personal(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.CharField(max_length=10)
    cargo = models.CharField(max_length=60)
    
    def __str__(self):
        return self.nombre + " - " + self.edad+ " - " +self.cargo

#----------------------------------------------

class cliente(models.Model):
    nombre = models.CharField(max_length=255)
    DNI = models.CharField(max_length=10)
    departamento = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=1,choices=TIPO_ESTADO)
    
    def __str__(self):
        return self.nombre + " - " + self.DNI+ " - " +self.departamento+ " - " +self.provincia+ " - " +self.fecha+ " - " +self.estado

class facturas(models.Model):
    ruc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    precio = models.DecimalField(max_digits = 10, decimal_places = 2)
    localidad = models.CharField(max_length=255)
    estado = models.CharField(max_length=1,choices=TIPO_ESTADO)

    def __str__(self):
        return self.ruc + " - " + self.nombre+ " - " +self.descripcion+ " - " +self.fecha+ " - " +self.precio+ " - " +self.localidad+ " - " +self.estado

class usuarios(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    correo_electronico = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre + " - " + self.apellidos+ " - " +self.correo_electronico+ " - " +self.contrasena
    

class contratos(models.Model):
    codigo = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=255)
    estado = models.CharField(max_length=2,choices=TIPO_CONTRATO)

    
    def __str__(self):
        return self.codigo + " - " + self.tipo+ " - " +self.nombre+ " - " +self.estado

