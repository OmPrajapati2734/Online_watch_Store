from django.urls import path
from Ecommerce_app.views import *

urlpatterns = [
    path('',first),
    path('login/',login, name='login'),
    path('logout/',logout,name='logout1'),
    path('register/',register,name='register'),
    path('table_all/',tableview_all),
    path('tableview_filter/',tableview_filter),
    path('index',index,name='index'),
    path('contact',contact,name='contact'),
    path('productall',productall,name='productall'),
    path('product-filter/<int:id>/',productCategoryWise,name='productfilter'),
    path('product-get/<int:id>/',singleproduct,name='productget'),
    path('phone/',phonelogin,name='phone'),
    path('forgotpassword/',ForgotPassword,name='forgotpassword'),
    path('changepassword/',ChangePassword,name='changepassword'),
    path('contactus/',contact,name='contactus'),
    # path('searchview/',searchview,name='search_view')
]