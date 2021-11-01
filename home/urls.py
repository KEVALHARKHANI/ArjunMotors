"""arjunmotor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from home import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',views.home,name='home'),
path('search',views.search,name='search'),
    path('wishlist',views.wl,name='wishlist'),
    path('add_to_wishlist',views.add_to_wishlist,name='add_to_wishlist'),
    path('move_to_product',views.move_to_product,name='move_to_product'),
    path('move_to_cart',views.move_to_cart,name='move_to_cart')
]
