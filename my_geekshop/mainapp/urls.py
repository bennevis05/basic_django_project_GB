from django.urls import path

import mainapp.views as mainapp

app_name = "mainapp"

urlpatterns = [
    path("", mainapp.catalog, name="main"),
    path("<int:pk>/", mainapp.category, name="category"),
    path("<int:category_pk>/<int:pk>/", mainapp.product, name="product"),
]
