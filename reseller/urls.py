from django.urls import path
from .import views

app_name = 'reseller'

urlpatterns = [
    path('resellerhome',views.reseller_home,name='reseller_home'),
    path('add_product',views.reseller_add_product,name='addproduct'),
    path('order_history',views.reseller_order_history,name='orderhistory'),
    path('cancelled_order',views.reseller_cancelled_order,name='cancelledorder'),
    path('recent_orders',views.reseller_recent_orders,name='recentorder'),
    path('change_password',views.reseller_change_password,name='changepass'),
    path('reseller_account',views.reseller_account,name='reselleraccount'),
    path('update_stock',views.reseller_update_stock,name='updatestock'),
    path('profile',views.profile,name= 'profile'),

]