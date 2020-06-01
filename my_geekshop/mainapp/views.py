from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import ProductCategory, Product
from basketapp.models import Basket
import random


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    return []


def main(request):
    title = 'технотрейд'
    basket = get_basket(request.user)
    content = {
        'title': title,
        'basket': basket
    }
    return render(request, 'mainapp/index.html', content)


def catalog(request):
    title = 'каталог'
    categories = ProductCategory.objects.all()
    basket = get_basket(request.user)
    hot_products = random.sample(list(Product.objects.all()), 2)
    content = {
        'title': title,
        'categories': categories,
        'basket': basket,
        'hot_products': hot_products
    }
    return render(request, 'mainapp/catalog/catalog.html', content)


def category(request, category_pk, page=1):
    title = 'категория'
    current_category = ProductCategory.objects.get(id=category_pk)
    products_category = Product.objects.filter(category__id=category_pk, is_active=True, category__is_active=True)
    basket = get_basket(request.user)

    paginator = Paginator(products_category, 2)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    content = {
        'title': title,
        'current_category': current_category,
        'products_category': products_paginator,
        'basket': basket
    }
    return render(request, 'mainapp/catalog/category.html', content)


def product(request, category_pk, product_pk):
    category = ProductCategory.objects.get(id=category_pk)
    product = Product.objects.get(id=product_pk)
    title = product.name
    basket = get_basket(request.user)
    content = {
        'title': title,
        'category': category,
        'product': product,
        'specifications': str(product.specifications).split(';'),
        'basket': basket
    }
    return render(request, 'mainapp/catalog/product.html', content)


def contact(request):
    title = 'контакты'
    basket = get_basket(request.user)
    email = 'support@tech.com'
    content = {
        'title': title,
        'basket': basket,
        'email': email
    }
    return render(request, 'mainapp/contact.html', content)
