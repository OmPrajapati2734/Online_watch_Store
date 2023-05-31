from django.urls import path
from Ecommerce_app.views import *

urlpatterns = [
    path('',first),
    path('login/',login, name='login'),
    path('logout/',logout,name='logout1'),
    path('forgot-passeord/',forgotpass,name='forgotpassword'),
    path('register/',register,name='register'),
    path('table_all/',tableview_all),
    path('tableview_filter/',tableview_filter),
    path('index',index,name='index'),
    path('contact',contact,name='contact'),
    path('productall',productall,name='productall'),
    path('product-filter/<int:id>/',productCategoryWise,name='productfilter'),
    path('product-get/<int:id>/',singleproduct,name='productget'),
    path('phone/',phonelogin,name='phone'),
    path('change-password/',ChangePassword,name='change'),
    path('contact-us',contact_us,name='contactus'),
    path('buy-now/',buynow,name='buy'),
    path('razorpayview/',razorpayView,name="razorpayview"),
    path('paymenthandler/',paymenthandler,name="paymenthandler"),
    path('successview/',successview,name="orderSuccessView"),
    path('order-list/',orderview,name="orderList")
    # path('searchview/',searchview,name='search_view')
]