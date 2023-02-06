from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .serializers import menuSerializer, bookingSerializer
from .models import Menu, Booking
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer