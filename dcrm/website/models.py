from django.db import models

# Create your models here. no habra necesidad de hacer SQL ya que todo se demine en
# este modulo
# con migrate se ejecuta y hace la base de datos: python manage.py makemigrations

class Record(models.Model):     # Model en mayuscula
    created_at = models.DateTimeField(auto_now_add=True)  # registro del tiempo automatico
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    phone =  models.CharField(max_length = 15)
    address = models.CharField(max_length = 100)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    zipcode = models.CharField(max_length = 20)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")





