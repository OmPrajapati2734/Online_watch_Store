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
class contactus(models.Model):
    name=models.CharField(max_length=200)
    Email=models.EmailField()
    Message=models.TextField()
    Phone=models.IntegerField()

class ordermodel(models.Model):
    productid=models.CharField(max_length=200)
    productqty=models.CharField(max_length=200)
    userId=models.CharField(max_length=200)
    userName=models.CharField(max_length=200)
    userEmail=models.EmailField()
    userContact=models.IntegerField()
    address=models.CharField(max_length=230)
    orderAmount=models.IntegerField()
    paymentMethod=models.CharField(max_length=200)
    transactionId=models.CharField(max_length=200)
    orderDate=models.DateTimeField(auto_created=True,auto_now=True)

def __str__(self):
    return self.userName