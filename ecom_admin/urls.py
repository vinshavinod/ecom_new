from django.urls import path
from .import views

app_name = 'ecom_admin'

urlpatterns = [
    path('adminhome',views.admin_home,name='admin_home'),
    path('approve_reseller',views.approve_reseller,name='approve_reseller'),
    path('change_password',views.change_password,name='changepass'),
    path('register_reseller',views.register_reseller,name='register_reseller'),
    path('admin_login',views.admin_login,name='admin_login'),
    path('status_approve/<int:reseller_id>',views.status_approve,name = 'status_approve'),
     

    

]