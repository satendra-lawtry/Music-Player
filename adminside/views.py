from django.shortcuts import render, redirect 
from app .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from adminside . models import Vender
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


def customerview(request):
    return render(request,'app/home.html')


def adminregistration(request):
    if request.method == "POST":
        shopemail = request.POST['shopemail']
        spassword = request.POST['spassword']
        ownername = request.POST['ownername']
        shopname = request.POST['shopname']
        registration_no = request.POST['registration_no']
        gstno = request.POST['gstno']
        shopcno = request.POST['shopcno']
        shopimage = request.POST['shopimage']
        shopadd = request.POST['shopadd']
        if Vender.objects.filter(registration_no=registration_no).exists():
            messages.warning(request,'Email id is Already Exists')
            return render(request,'adminapp/adminregistrationform.html')
        else:
            user = Vender.objects.create(shopemail=shopemail, spassword=spassword,ownername=ownername, shopname=shopname,
                                         gstno=gstno,shopcno=shopcno,registration_no=registration_no,
                                         shopimage=shopimage,shopadd=shopadd)
            user.save()
            messages.info(request,'Profile Created Successfully')
            return render (request,'adminapp/adminlogin.html')
    else:
        return render(request,'adminapp/adminregistrationform.html')

# @login_required
def adminprofile(Request):
    data = Vender.objects.all()
    return render(Request,'adminapp/admindetails.html',{'data': data})

def admindetails(request):
    return render(request,'adminapp/admindetails.html')


def adminlogin(request):
    v = Vender.objects.all()
    if request.method == 'POST':
        v.shopemail = request.POST['shopemail']
        v.spassword = request.POST['spassword']
        user = auth.authenticate(shopemail=v.shopemail,spassword=v.spassword)
        if user is not None:
            auth.login(request, user)
            messages.success(request,'Login succesfull')
            return render (request,'adminapp/adminprofile.html')
        else:
            messages.warning(request,'Invalid Registration or Password')
            return render (request,'adminapp/adminlogin.html')
    return render(request,'adminapp/adminlogin.html')


# @login_required
def adminaddproduct(request):
    if request.method == 'POST':
        title = request.POST['title']
        selling_price = request.POST['selling_price']
        discounted_price = request.POST['discounted_price']
        brand = request.POST['brand']
        description = request.POST['description']
        category = request.POST['category']
        product_image = request.POST['product_image']
        add_product = Product(title=title,selling_price=selling_price,discounted_price=discounted_price,
                                        brand=brand,description=description,category=category,product_image=product_image)
        add_product.save()
        messages.success(request,'Product added successfully')
        return render (request,'adminapp/adminaddproduct.html')
    return render(request,'adminapp/adminaddproduct.html')

def adminlogout(request):
    return redirect('adminlogin')

