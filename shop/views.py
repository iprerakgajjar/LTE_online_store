from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Order
from math import ceil
import pymysql
from pymysql import *

def index(request):
    #products=Product.objects.all()
    #print(products)
    #n=len(products)
    #nslides=ceil(n/4) #no of slides
    #params={'no_of_slides':nslides,'range':range(1,nslides),'product':products}
    allproducts=[]
    prodcat=Product.objects.values('category','id')
    categorys={item['category'] for item in prodcat}
    for c in categorys:
        prods=Product.objects.filter(category=c)
        n=len(prods)
        nslides=ceil(n/4)
        allproducts.append([prods,range(1,nslides),nslides])
    params={'allprods':allproducts}
    return render(request,'shop/index.html',params)

def aboutus(request):
    return render(request,'shop/about.html')

def contactus(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        feedback=request.POST.get('feedback', '')
        print(name, email, phone, feedback)
        contact=Contact(name=name,email=email,phone=phone,feedback=feedback)
        contact.save()
    return render(request,'shop/contact.html')

def product(request,pid):
    pro=Product.objects.filter(id=pid)
    return render(request,'shop/products.html',{'product':pro[0]})

def cart(request):
    return HttpResponse("This is Add to Cart Page")

def order(request):
    if request.method=="POST":
        cartjson=request.POST.get('cartjson','')
        fname=request.POST.get('firstname','')
        lname=request.POST.get('lastname','')
        email=request.POST.get('email','')
        address1=request.POST.get('address1','')
        address2=request.POST.get('address2','')
        phone=request.POST.get('mobileno','')
        state=request.POST.get('state','')
        city=request.POST.get('city','')
        zip=request.POST.get('zip','')
        order=Order(item_json=cartjson,fname=fname,lname=lname,email=email,address1=address1,address2=address2,phone=phone,state=state,city=city,zip=zip)
        order.save()
        flag=True
        return render(request,'shop/order.html',{'flag':flag})
    return render(request,'shop/order.html')