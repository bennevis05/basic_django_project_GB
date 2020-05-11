from django.shortcuts import render

links_menu = [
        {'href': 'main', 'name': 'Главная'},
        {'href': 'product', 'name': 'Каталог'},
        {'href': 'contact', 'name': 'Контакты'},
]

def main(request):
    title = 'технотрейд'
    content = {'title': title, 'links_menu': links_menu}
    return render(request, 'mainapp/index.html', content)


def product(request):
    title = 'geforce rtx 2080'
    content = {'title': title, 'links_menu': links_menu}
    return render(request, 'mainapp/product.html', content)


def contact(request):
    title = 'контакты'
    content = {'title': title, 'links_menu': links_menu}
    return render(request, 'mainapp/contact.html', content)
