from django.shortcuts import render

from reseller.models import Product, Reseller

# Create your views here.

def reseller_home(request):
    seller = Reseller.objects.get(id = request.session['s_id'])
    return render(request,'reseller/reseller_home.html',{'seller_details':seller})

def reseller_add_product(request):
    msg = " "
    if request.method == 'POST':
        product_category = request.POST['p_cat']
        product_name = request.POST['p_name']
        product_number = request.POST['p_no']
        product_description = request.POST['p_desc']
        product_price = request.POST['p_price']
        product_stock = request.POST['p_stock']
        product_image = request.FILES['p_img']

        product_exist =Product.objects.filter(p_number = product_number).exists()
        if not product_exist:
            product = Product(
                p_category = product_category,
                p_name = product_name,
                p_number = product_number,
                p_price = product_price,
                p_description = product_description,
                p_stock = product_stock,
                p_image = product_image,
                seller_id_id = request.session['s_id']
            ) 
            product.save()
            msg = "product added succesfully"
        
        else:
            msg = "product already added"



    return render(request,'reseller/add_product.html',{'status':msg})

def reseller_cancelled_order(request):
    return render(request,'reseller/cancelled_order.html')

def reseller_change_password(request):
    return render(request,'reseller/change_password.html')

def reseller_order_history(request):
    return render(request,'reseller/order_history.html')

def reseller_account(request):
    return render(request,'reseller/reseller_account.html')

def reseller_update_stock(request):
    return render(request,'reseller/update_stock.html')

def reseller_recent_orders(request):
    return render(request,'reseller/recent_orders.html')

def reseller_product_catelogue(request):
    
    return render(request,'reseller/product_catelogue.html')

def profile(request):
    seller_list = Reseller.objects.get(id = request.session['s_id'])
    
    return render(request,'reseller/profile.html',{'seller_list':seller_list})





