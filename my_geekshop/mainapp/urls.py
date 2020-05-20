from django.urls import path

import mainapp.views as mainapp

app_name = "mainapp"

urlpatterns = [
    path("", mainapp.catalog, name="main"),
    path("<int:category_pk>/", mainapp.category, name="category"),
    path("<int:category_pk>/<int:product_pk>/", mainapp.product, name="product"),
]
