# restaurant/urls.py
from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers
from .serializers import *

# Create a router and register your viewset with it.
router = routers.DefaultRouter()
#router.register(r'your-model', YourModelViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    path('login/', views.login, name='login')
]