from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ItemSerializer
from .models import Item

# Create your views here.
class ItemViewSet(ModelViewSet):
    serializer_class=ItemSerializer
    queryset=Item.objects.all()
    
