from .models import Menu,Booking
from .serializers import MenuSerializer,BookSerializer,UserSerializer
from django.shortcuts import render
from rest_framework import generics,viewsets
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return render(request, 'index.html', {})


class MenuItemView (generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView (generics.RetrieveUpdateDestroyAPIView):
    queryset =Menu
    serializer_class = MenuSerializer

class BookingViewSet (viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated]