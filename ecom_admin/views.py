from django.shortcuts import redirect, render
from customer.models import Customer

from ecom_admin.models import AdminLogin
from django.core.mail import send_mail
from django.conf import settings

from reseller.models import Reseller

# Create your views here.


# import settings and send mail modules


def admin_home(request):
    #taking the count of items in customer and seller table and using count method assign the count of items in to the variables 
    seller_count = Reseller.objects.all().count()
    customer_count = Customer.objects.all().count()
    return render(request,'ecom_admin/admin_home.html',{'seller_count':seller_count,'customer_count':customer_count})

def approve_reseller(request):
    reseller = Reseller.objects.filter(status = "pending")
    return render(request,'ecom_admin/approve_resellers.html',{'pending':reseller})

    #creating an object named reseller - filter resellers from database where status pending and then pass the datas to the admins approve reseller page

def status_approve(request,reseller_id):
    reseller = Reseller.objects.filter(id = reseller_id).update(status = "approved")
    new_reseller = Reseller.objects.get(id = reseller_id)
    subject = 'welcome to ecommerce world'
    message = f'Hi {new_reseller.s_name},Thank you for registering in ecommerce application'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['farhafinu36@gmail.com']
    send_mail(subject,message,email_from,recipient_list)
    return redirect('ecom_admin:approve_reseller')

    #status_approve is the function for approve button in the action column in the approve reseller table @admin 
    #create an object reseller filter with session id and update it status to approved 
    # then when the admin press the approve button the status approve and at the moment an email is send to the resellers registred email id
    #for that creating an object new_reseller with session id getting details
    #here email_host_user :is vinisha -mail id  which is given in project settings emailbackend confg
    # recipient list = sellers mail id 

def change_password(request):
    return render(request,'ecom_admin/change_password.html')

def register_reseller(request):
    reseller_list = Reseller.objects.all()
    # creating reseller list object to pass datas of reseller to admin view @registered resellers
    return render(request,'ecom_admin/register_reseller.html',{'resellers': reseller_list})

def admin_login(request):
    if request.method == 'POST':
        if 'signin' in request.POST:
            admin_id = request.POST['a_id']
            admin_password = request.POST['a_pass']
            print('data')

            try:

                print('test')
                admin_login = AdminLogin.objects.get(admin_id = admin_id,admin_password = admin_password)#approve
                request.session['s_id'] = admin_login.id
                return redirect("ecom_admin:admin_home")# redirect is used to redirect to html page in another module "here reseller module"
            except:
                error_msg = 'invalid username or password'
                return render(request,'ecom_admin/admin_login.html',{'error_msg':error_msg})

    return render(request,'ecom_admin/admin_login.html')