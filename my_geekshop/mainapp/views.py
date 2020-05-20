from django.shortcuts import render
from .models import ProductCategory, Product
from basketapp.models import Basket


def main(request):
    title = 'технотрейд'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    content = {
        'title': title,
        'basket': basket
    }
    return render(request, 'mainapp/index.html', content)


def catalog(request):
    title = 'каталог'
    categories = ProductCategory.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    content = {
        'title': title,
        'categories': categories,
        'basket': basket
    }
    return render(request, 'mainapp/catalog/catalog.html', content)


def category(request, category_pk):
    title = 'категория товара'
    current_category = ProductCategory.objects.get(id=category_pk)
    products_category = Product.objects.filter(category__id=category_pk)
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    content = {
        'title': title,
        'current_category': current_category,
        'products_category': products_category,
        'basket': basket
    }
    return render(request, 'mainapp/catalog/category.html', content)


def product(request, category_pk, product_pk):
    product = Product.objects.get(id=product_pk)
    title = product.name
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    content = {
        'title': title,
        'product': product,
        'specifications': str(product.specifications).split(';'),
        'basket': basket
    }
    return render(request, 'mainapp/catalog/product.html', content)


def contact(request):
    title = 'контакты'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    content = {
        'title': title,
        'basket': basket
    }
    return render(request, 'mainapp/contact.html', content)
