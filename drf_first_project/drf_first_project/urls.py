"""
URL configuration for drf_first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from women import views
from rest_framework import routers, urls


#from women.views import WomenViewSet

# задаем маршруты через роутеры
# router = routers.DefaultRouter()
# router.register(r'women', WomenViewSet)

#можно создавать и свои классы роутеров

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('api/v1/', include(router.urls)) #http://127.0.0.1:8000/api/v1/women/
    path('api/v1/women/', views.WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', views.WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', views.WomenAPIDetailView.as_view()),
    # аутентификация через djoser
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
