from django.db import models

# Create your models here.


class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name= models.CharField(max_length=150)
    last_name= models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=30)
    adress = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"