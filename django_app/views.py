from django.shortcuts import render, redirect

from .forms import *
from .models import *


def index(request) :
    categories = Category.objects.all ()
    products = Product.objects.all ()
    context = {
        'categories' : categories,
        'products' : products,
    }
    return render ( request, 'index.html', context )


def categories(request) :
    categories = Category.objects.all ()
    return render ( request, 'categories.html', {'categories' : categories} )


def categories_with_id(request, category_id) :
    categories = Category.objects.filter ( category_id=category_id )
    return render ( request, 'categories.html', {'categories' : categories} )


def products(request) :
    products = Product.objects.all ()
    categories = Category.objects.all ()
    context = {
        'products' : products,
        'categories' : categories
    }
    return render ( request, 'products.html', context )


def products_by_category(request, category_id) :
    products = Product.objects.filter ( category_id=category_id )
    categories = Category.objects.all ()
    return render ( request, 'products.html', {'products' : products, 'categories' : categories} )


def suppliers(request) :
    suppliers = Supplier.objects.all ()
    return render ( request, 'suppliers.html', {'suppliers' : suppliers} )


def add_news(request) :
    if request.method == 'POST' :
        print ( "==============", request.POST )
        print ( "==============", request.FILES )
        form = NewsForm ( request.POST, request.FILES )
        if form.is_valid () :
            form.save ()
            return redirect ( 'index' )
    else :
        form = NewsForm ()
    return render ( request, 'add_news.html', {'form' : form} )


def add_category(request) :
    if request.method == 'POST' :
        print ( "==============", request.POST )
        print ( "==============", request.FILES )
        form = CategoryForm ( request.POST, request.FILES )
        if form.is_valid () :
            form.save ()
            return redirect ( 'index' )
    else :
        form = CategoryForm ()
    return render ( request, 'add_category.html', {'form' : form} )


def add_product(request) :
    if request.method == 'POST' :
        print ( "==============", request.POST )
        print ( "==============", request.FILES )
        form = ProductForm ( request.POST, request.FILES )
        if form.is_valid () :
            form.save ()
            return redirect ( 'index' )
    else :
        form = ProductForm ()
    return render ( request, 'add_product.html', {'form' : form} )


def add_supplier(request) :
    if request.method == 'POST' :
        print ( "==============", request.POST )
        print ( "==============", request.FILES )
        form = SupplierForm ( request.POST, request.FILES )
        if form.is_valid () :
            form.save ()
            return redirect ( 'index' )
    else :
        form = SupplierForm ()
    return render ( request, 'add_supplier.html', {'form' : form} )
