from django.shortcuts import render
from .models import ProductCategory, Product


def main(request):
    title = 'технотрейд'
    content = {'title': title}
    return render(request, 'mainapp/index.html', content)


def catalog(request, pk=None):
    title = 'каталог'
    categories = ProductCategory.objects.all()
    products = Product.objects.all()
    content = {
            'title': title,
            'categories': categories,
            'products': products
    }
    if pk:
        category = ProductCategory.objects.all()[pk - 1]
        try:
            products = Product.objects.filter(category_id = category.id)
            content = {
                'title': title,
                'category': category,
                'products': products
            }
        except IndexError:
            products = 'Товары пока отсутствуют'
            content = {
                'title': title,
                'category': category,
                'products': products
            }
        return render(request, f'mainapp/catalog/category.html', content)
    return render(request, 'mainapp/catalog/catalog.html', content)


def product(request, pk=None):
    category = ProductCategory.objects.all()[pk - 1]
    product = Product.objects.all()[pk - 1]
    title = product.name
    content = {
        'title': title,
        'category': category,
        'product': product,
        'specifications': str(product.specifications).split(';')
    }
    return render(request, 'mainapp/catalog/product.html', content)


def contact(request):
    title = 'контакты'
    content = {'title': title}
    return render(request, 'mainapp/contact.html', content)
