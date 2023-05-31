from django.contrib import admin

from Ecommerce_app.models import *

# Register your models here.
class blogregister(admin.ModelAdmin):
    list_display=['name','tagline']
    list_filter=['name','tagline']
    search_fields=['name','tagline']


admin.site.register(Categoryregister)

admin.site.register(Product)

class Productregister(admin.ModelAdmin):
    product_display=['Product_name','img','price','Quantity']
    product_filter=['Product_name','price']

admin.site.register(UserReg)

class UserRegister(admin.ModelAdmin):
    list_display=['name','Email']


class ContactRegister(admin.ModelAdmin):
    contact_display=['name','Email','Phone']
admin.site.register(contactus)

admin.site.register(ordermodel)


