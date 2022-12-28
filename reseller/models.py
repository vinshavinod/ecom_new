from datetime import date
from django.db import models

# Create your models here.

class Reseller(models.Model):
    s_name = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    email = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20)
    account_holder_name = models.CharField(max_length=20)
    account_number = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=20)
    upload_image = models.ImageField(upload_to = 'reseller/')
    password = models.CharField(max_length=20)
    status = models.CharField(max_length=12,default="pending")

class Product(models.Model):
    seller_id = models.ForeignKey(Reseller,on_delete=models.CASCADE)
    p_category = models.CharField(max_length=40)
    p_name = models.CharField(max_length=40)
    p_number = models.BigIntegerField()
    p_price = models.BigIntegerField()
    p_description = models.CharField(max_length=500,default="")
    p_stock = models.BigIntegerField()
    p_image = models.ImageField(upload_to='product/')
    date = models.DateField(default=date.today)
