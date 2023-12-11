from django.shortcuts import render
from .forms import BookingForm
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework import viewsets, permissions
from .serializers import *
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def menu(request):
    return render(request, 'menu.html', {})

def book(request):
    form = BookingForm()
    if form.is_valid():
            form.save()    
    context = {'form':form}
    return render(request, 'book.html', context)

def login(request):
    return render(request, 'login.html', {})




class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    
class SingleItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]