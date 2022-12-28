from django.urls import path
from .import views

app_name = 'customer'

urlpatterns = [
    path('',views.customer_home,name='home'),
    path('login',views.customer_login,name='login'),
    path('myorder',views.customer_myorder,name='myorder'),
    path('my_wishlist',views.customer_mywishlist,name='mywhishlist'),
    path('modal',views.modal,name='modal'),
    path('login1',views.login1,name='login1'),
    path('signup',views.signup,name='signup'),
    path('my_account',views.customer_my_account,name='myaccount'),
    path ('c_logout',views.logout,name= 'c_logout'),
    path('profile',views.profile,name= 'profile'),
    path('detail/<int:product_id>',views.detail,name='p_detail'),
    path('detail1',views.detail1,name='detail1'),
    
]