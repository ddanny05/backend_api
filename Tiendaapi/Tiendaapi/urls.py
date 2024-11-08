"""
URL configuration for Tiendaapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Ventasapi.views import ClienteViewSet

router = DefaultRouter() #variable que contiene a la clase default router q pemite crear cada una de las rutas de mi api
router.register(r'cliente', ClienteViewSet) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls) ),  #agrego la ruta base de mi api a la lista de urls
]
