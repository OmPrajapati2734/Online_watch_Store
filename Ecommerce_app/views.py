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
            contact1=contactus()
            contact1.name=request.POST['name']
            contact1.Email=request.POST['email']
            contact1.Phone=request.POST['phone']
            contact1.Message=request.POST['message']
            contact1.save()
            return render(request,'contact.html',{'message':"Message sent successfully",'a':a})
        return render(request,'contact.html',{'data':data,'a':a})
    else:
        if request.method == "POST":
            contact1=contactus()
            contact1.name=request.POST['name']
            contact1.Email=request.POST['email']
            contact1.Phone=request.POST['phone']
            contact1.Message=request.POST['message']
            contact1.save()
            return render(request,'contact.html',{'message':"Message sent successfully"})
        return render(request,'contact.html')

import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

def buynow(request):
    if 'email' in request.session:
        a=UserReg.objects.get(Email=request.session['email'])
        if request.method == "POST":
            request.session['productid']=request.POST['id']
            request.session['quantity']="1"
            request.session['userid']=a.pk
            request.session['username']=a.name
            request.session['userEmail']=a.Email
            request.session['userContact']=a.Phone
            request.session['address']=a.Address
            b=Product.objects.get(id=request.POST['id'])
            request.session['orderAmount']=b.price
            request.session['paymentMethod']="Razorpay"
            request.session['transactionId']=""
            return redirect('razorpayview')
    else:
        return redirect('login')


RAZOR_KEY_ID = 'rzp_test_UOVF2HrT4Rsqtn'
RAZOR_KEY_SECRET = 'Yvx0tTc0eBU0L64czzDOFWzR'
client = razorpay.Client(auth=(RAZOR_KEY_ID,RAZOR_KEY_SECRET))   


def razorpayView(request):
    currency = 'INR'
    amount = int(request.session['orderAmount'])*100
    # Create a Razorpay Order
    razorpay_order = client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'http://127.0.0.1:8000/paymenthandler/'    
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url    
    return render(request,'razorpayDemo.html',context=context)


@csrf_exempt
def paymenthandler(request):
    # only accept POST request.
    if request.method == "POST":
        try:
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')

            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = client.utility.verify_payment_signature(
                params_dict)
            
            amount = int(request.session['orderAmount'])*100  # Rs. 200
            # capture the payemt
            client.payment.capture(payment_id, amount)

            #Order Save Code
            orderModel = ordermodel()
            orderModel.productid=request.session['productid']
            orderModel.productqty=request.session['quantity']
            orderModel.userId = request.session['userid']
            orderModel.userName = request.session['username']
            orderModel.userEmail = request.session['userEmail']
            orderModel.userContact = request.session['userContact']
            orderModel.address = request.session['address']
            orderModel.orderAmount = request.session['orderAmount']
            orderModel.paymentMethod = request.session['paymentMethod']
            orderModel.transactionId = payment_id
            # this function is for quantity of product when cutomer buys product it will deduct it from main quantity.
            productdata=Product.objects.get(id=request.session['productid'])
            productdata.Quantity=productdata.Quantity-int(request.session['quantity'])
            productdata.save()
            orderModel.save()
            del request.session['productid']
            del request.session['quantity']
            del request.session['userid']
            del request.session['username']
            del request.session['userEmail']
            del request.session['userContact']
            del request.session['address']
            del request.session['orderAmount']
            del request.session['paymentMethod']
            # render success page on successful caputre of payment
            return redirect('orderSuccessView')
        except:
            print("Hello")
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        print("Hello123")
       # if other than POST request is made.
        return HttpResponseBadRequest()  

def successview(request):
    if 'email' in request.session:
        a=request.session['email']
        return render(request,'order_success.html',{'a':a})
    else:
        return HttpResponseBadRequest()
    
def orderview(request):
    if 'email' in request.session:
        a=request.session['email']
        data=ordermodel.objects.filter(userEmail=a)
        prolist=[]
        for i in data:
            pro={}
            productdata=Product.objects.get(id=i.productid)
            pro['name']=productdata.Product_name
            pro['img']=productdata.img
            pro['price']=i.orderAmount
            pro['quantity']=i.productqty
            pro['date']=i.orderDate
            pro['TransactionId']=i.transactionId
            prolist.append(pro)
        return render(request,'ordertable.html',{'a':a,'prolist':prolist})
    else:
        return HttpResponseBadRequest()
    
def forgotpass(request):
    return render(request,'fordotpass.html')
