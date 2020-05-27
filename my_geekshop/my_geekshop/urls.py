from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path
import mainapp.views as mainapp

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('catalog/', include('mainapp.urls', namespace='catalog')),
    path('contact/', mainapp.contact, name='contact'),
    path('auth/', include('authnapp.urls', namespace='auth')),
    path("basket/", include("basketapp.urls", namespace="basket")),
    path("admin/", include("adminapp.urls", namespace="admin")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
