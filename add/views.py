from django.shortcuts import render,redirect
from home.models import Products
from django.contrib import messages

# Create your views here.

def add(request):
    return render(request,'add.html')

def product(request):
    number = int(request.POST['number'])
    ls=''
    for i in range(number):
        ls=ls+str(i)
    return render(request,'add.html',{'num':ls,'num_len':number})

def save(request):
    number = int(request.POST['number'])
    for i in range(number):
        product = request.POST['product'+str(i)]
        car = request.POST['car'+str(i)]
        category = request.POST['category'+str(i)]
        quantity = request.POST['quantity'+str(i)]
        price = request.POST['price'+str(i)]
        description = request.POST['description'+str(i)]
        location = request.POST['location'+str(i)]
        image= request.FILES
        pd = Products(product=product,car=car,category=category,quantity=quantity,price=price,description=description,location=location,photo=image['image'+str(i)])
        pd.save()
    messages.add_message(request,messages.INFO,'data saved successfully')
    return redirect('/add')



