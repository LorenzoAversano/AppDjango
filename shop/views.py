from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# from .models import Question

def index(request):
    return render(request, 'shop/index.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'shop/products.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        products = Product.objects.all()
        return render(request, 'shop/products.html', {'products': products})
    else:
        form = ProductForm()
    return render(request, 'shop/add_product.html', {'form': form})

def update_product(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('../../products')
    context = {'form': form}
    return render(request, 'shop/update_product.html', context)

def delete_product(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('../../products')
    context = {'item': product}
    return render(request, 'shop/delete_product.html', context)

def view_product(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'shop/view_product.html', context)