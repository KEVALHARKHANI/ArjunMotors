from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect,HttpResponse
from home.models import Products
from .models import Cart
# Create your views here.
def cart(request):
    result_list = []
    total = 0
    cproduct = Cart.objects.select_related('pid').all()
    for i in cproduct:
        total+=(i.pid.price*i.wquantity)
    print(total)
    return render(request,"Cart.html",{'results':cproduct,'total':total})

def quantity_update(request):
    id= request.GET["id"]
    q = int(request.GET["q"])
    cproduct = Cart.objects.get(id= id)
    cproduct.wquantity = q
    cproduct.save()
    return HttpResponse("quantity update successfully")

def price_update(request):
    total = 0
    cproduct = Cart.objects.select_related('pid').all()
    for i in cproduct:
        total += (i.pid.price * i.wquantity)
    print(total)
    return HttpResponse(total)

def item_remove(request):
    id= request.GET["id"]
    cid = Cart.objects.get(id=id)
    cid.delete()
    return redirect('/cart')

def checkout(request):
    try:
        cproduct = Cart.objects.select_related('pid').all()
        for i in cproduct:
            p = Products.objects.get(id=i.pid.id)
            p.quantity = p.quantity - i.wquantity
            p.save()
        cproduct.delete()
        return redirect('/cart')
    except ObjectDoesNotExist:
        return redirect('/')