from django.urls.conf import include
from django import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('formularios/', include('projeto.urls')),
    path('menu/', include('projeto.urls')),
]
