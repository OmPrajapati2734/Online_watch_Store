from django.shortcuts import render,redirect
from django.http import HttpResponse
from Ecommerce_app.models import *

# Create your views here.
def first(request):
    return HttpResponse('<h1>Hello this is first HTML page with django</h1>')

def login(request):
    if request.method == "POST":
        email1=request.POST['email']
        password1=request.POST['password']
        try:
            data=UserReg.objects.get(Email=email1,Password=password1)
            if data:
                request.session['email']=data.Email
                return redirect('index')
            else:
                return render(request,'login.html',{'message':"Invalid Email or Password"})
        except:
            return render(request,'login.html',{'message':"Invalid Email or Password"})
        
    return render(request,'login.html')

def logout(request):
    if 'email' in request.session.keys():
        del request.session['email']
        return redirect('index')
    else:
        return redirect('index')

        

def tableview_all(request):
    a=UserReg.objects.all()
    print("data",a)
    return render(request,'table.html',{"data": a})

def tableview_filter(request):
    a=UserReg.objects.filter(Phone=9876543210)
    print("data",a)
    return render(request,'table.html',{"data": a})

def index(request):
    if 'email' in request.session:
        a=request.session['email']
        data=Categoryregister.objects.all()
        return render(request,'index.html',{'data':data,'a':a})
    else:
        data=Categoryregister.objects.all()
        return render(request,'index.html',{'data':data})
 

def contact(request):
    return render(request,'contact.html')

#this function for products only
def productall(request):
    if 'email' in request.session:
        a=request.session['email']
        data=Product.objects.all()
        return render(request,'productall.html',{'data':data,'a':a})
    else:
       data=Product.objects.all()
       return render(request,'productall.html',{'data':data})

#this function for products which can be filtered by their category and displayed on product page.
def productCategoryWise(request,id):
     if 'email' in request.session:
        a=request.session['email']
        data=Product.objects.filter(categoryname=id)
        return render(request,'productall.html',{'data':data,'a':a})
     else:
         data=Product.objects.filter(categoryname=id)
         return render(request,'productall.html',{'data':data})

#this function for single products which are seleceted after category selection.
def singleproduct(request,id):
    if 'email' in request.session:
        a=request.session['email']
        data=Product.objects.get(pk=id)
        return render(request,'singleproduct.html',{'data':data,'a':a})
    else:
        data=Product.objects.get(pk=id)
        return render(request,'singleproduct.html',{'data':data})

def register(request):
    if request.method=="POST":
        name1 =request.POST['uname']
        email1 =request.POST['email']
        password1 =request.POST['password']
        address1 =request.POST['address']
        phone1 =request.POST['phone']
        print(name1,email1,password1,address1,phone1)
        data=UserReg(name=name1,Email=email1,Password=password1,Address=address1,Phone=phone1)
        a=UserReg.objects.filter(Email=email1)
        if len(a)==0:
            data.save()
            return redirect('login')
        else:
            return render(request,'register.html',{'message':"User email is already used!!"})
        
    return render(request,'register.html')

def phonelogin(request):
    return render(request,'phone.html')

def ForgotPassword(request):
    return render(request,'forgotpass.html')

def ChangePassword(request):
    if 'email' in request.session:
        a=request.session['email']
        user=UserReg.objects.get(Email=a)
        if request.method=="POST":
           old=request.POST['old_password']
           newpass=request.POST['newpassword']
           newpass2=request.POST['confirmpassword']
           if(old==UserReg.Password):
               if(newpass==newpass2):
                   UserReg.Password=newpass
                   UserReg.save()
                   return render(request,'changepass.html',{'message':"password updated successfully"})
               else:
                   return render(request,'changepass.html',{'message':"New Password does not match"})
           else:
               return render(request,'changepass.html',{'message':"old Password does not match"})
                   
        return render(request,'changepass.html',{'a':a})
    else:
        return render('login')
    

def contact_us(request):
    if 'email' in request.session:
        a=request.session['email']
        data=UserReg.objects.get(Email=a)
        if request.method == "POST":
            contact1=Contact()
            contact1.name=request.POST['name']
            contact1.Email=request.POST['email']
            contact1.Phone=request.POST['phone']
            contact1.Message=request.POST['message']
            contact1.save()
            return render(request,'contact.html',{'message':"Message sent successfully",'a':a})
        return render(request,'contact.html',{'data':data,'a':a})
    else:
        if request.method == "POST":
            contact1=Contact()
            contact1.name=request.POST['name']
            contact1.Email=request.POST['email']
            contact1.Phone=request.POST['phone']
            contact1.Message=request.POST['message']
            contact1.save()
            return render(request,'contact.html',{'message':"Message sent successfully"})
        return render(request,'contact.html')
    
# from django.db.models import Q
# def searchview(request):
#     word=request.GET.get('search')
#     wordset=word.split(" ")
#     for i in wordset:
#         b=Product.objects.filter(Q(Product_name__categoryname__icontains=i)|Q(Product_name__icontains=i)|Q(price__icontains=i)).distinct()
#         return render(request,'productall.html',{'data':b})