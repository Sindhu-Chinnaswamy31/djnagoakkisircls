from django.db import models

# Create your models here.

class Customer_data(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=100,unique=True)
    PhoneNo=models.CharField(max_length=10,unique=True)
    Subject=models.CharField(max_length=200)
    Message=models.CharField(max_length=500)
    Comment=models.CharField(max_length=200)

    def __str__(self):
        return self.Name



