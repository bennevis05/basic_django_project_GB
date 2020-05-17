from django.shortcuts import render
from .models import ProductCategory, Product


def main(request):
    title = 'технотрейд'
    content = {'title': title}
    return render(request, 'mainapp/index.html', content)


def catalog(request):
    title = 'каталог'
    categories = ProductCategory.objects.all()
    content = {
        'title': title,
        'categories': categories
    }
    return render(request, 'mainapp/catalog/catalog.html', content)


def category(request, category_pk):
    title = 'категория товара'
    current_category = ProductCategory.objects.get(id=category_pk)
    products_category = Product.objects.filter(category_id=category_pk)
    content = {
        'title': title,
        'current_category': current_category,
        'products_category': products_category
    }
    return render(request, 'mainapp/catalog/category.html', content)


def product(request, category_pk, product_pk):
    product = Product.objects.get(id=product_pk)
    title = product.name
    content = {
        'title': title,
        'product': product,
        'specifications': str(product.specifications).split(';')
    }
    return render(request, 'mainapp/catalog/product.html', content)


def contact(request):
    title = 'контакты'
    content = {'title': title}
    return render(request, 'mainapp/contact.html', content)
