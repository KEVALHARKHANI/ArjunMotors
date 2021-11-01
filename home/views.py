from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect,HttpResponse
from .models import Products
from django.db.models import Q
from django.contrib import messages
from Cart.models import Cart
# Create your views here.
def home(request):
    return render(request,'index.html')

def search(request):
    srch=str(request.GET['keywords'])
    ls=srch.split(' ')
    final_list=[]
    for q in ls:
        result = list(Products.objects.filter(Q(product__icontains=q)|
                                              Q(car__icontains=q)|
                                              Q(category__icontains=q)|
                                              Q(description__icontains=q)
                                               ).filter(wishlist=False))
        final_list.append(result)
    print(final_list)
    common=com(final_list)
    print(common)
    return render(request,'index.html',{'result':common,'srch':srch})

def com(ls):
    com=list(set.intersection(*map(set,ls)))
    return com

def wl(request):
    result = Products.objects.filter(wishlist=True)

    return render(request,'wishlist.html',{'product':result,'num_len':len(result)})

def add_to_wishlist(request):
    product = request.POST['product']
    car = request.POST['car']
    category = request.POST['category']
    quantity = request.POST['quantity']
    description = request.POST['description']

    pd = Products(product=product,car=car,category=category,wquantity=quantity,description=description,wishlist=True)
    pd.save()
    messages.add_message(request,messages.INFO,'data added successfully')
    return redirect('/wishlist')

def move_to_product(request):
    items=request.POST['items']
    images=request.FILES
    print('image:',images)
    print(items)
    ls=items.split('-')
    print('list :',ls)
    for l in ls[:len(ls)-1]:
        price=int(request.POST['price'+l])
        quantity = int(request.POST['quantity' + l])
        location = str(request.POST['location' + l])
        item=Products.objects.get(id=l)
        item.wishlist=False
        item.price=price
        item.quantity=quantity
        item.location=location
        item.photo=images['photo'+l]
        item.save()
    messages.add_message(request,messages.INFO,'data added successfully')
    return redirect('/wishlist')

def move_to_cart(request):
    pid = request.GET['pid']
    print(pid)
    product_instance = Products.objects.get(id=pid)
    print(product_instance)
    try:
        product_in_cart = Cart.objects.get(pid=product_instance)
        if product_in_cart:
            product_in_cart.wquantity +=1
            product_in_cart.save()
        else:
            cart = Cart(pid = pid,wquantity = 1)
            cart.save()
    except ObjectDoesNotExist:
        cart = Cart(pid=product_instance, wquantity=1)
        cart.save()

    return HttpResponse("add to cart successfully")






