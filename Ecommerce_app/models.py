from datetime import date

from django.db import models

    
class Categoryregister(models.Model):
    categoryname = models.CharField(max_length=200)
    img=models.ImageField(upload_to='category')

    def __str__(self):
        return self.categoryname

class Product(models.Model):
    categoryname = models.ForeignKey(Categoryregister,on_delete=models.CASCADE)
    Product_name = models.CharField(max_length=200)
    img=models.ImageField(upload_to='product')
    P_description=models.CharField(max_length=200)
    price=models.IntegerField()
    Quantity=models.IntegerField()

#This table is for User_Reagisteration
class UserReg(models.Model):
    name=models.CharField(max_length=200)
    Email=models.EmailField()
    Password=models.CharField(max_length=100)
    Address=models.CharField(max_length=250)
    Phone=models.IntegerField()
    
#This table is for contact us 
class Contact(models.Model):
    name=models.CharField(max_length=200)
    Email=models.EmailField()
    Subject=models.CharField(max_length=100)
    Message=models.CharField(max_length=250)
    Phone=models.IntegerField()