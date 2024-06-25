from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm


#CRUD
def home(request):
    products = Product.objects.all()
    return render(request,'home.html',{'productslist':products})
    #return HttpResponse("Hello Guys! This is our first response to the url request...")

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Data stored successfully......")
    else:
        form = ProductForm()
    return render(request,"add_product.html",{'form':form})

def update_product(request, product_id):
    product = get_object_or_404(Product, id =product_id)
    if request.method == "POST":
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return HttpResponse("Data updated successfully......")
    else:
        form = ProductForm(instance=product)
    return render(request,"update_product.html",{'form':form})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        return HttpResponse("Data deleted successfully......")
    return render(request,"delete_product.html",{'product':product})



