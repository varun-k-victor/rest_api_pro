#from django.shortcuts import render
from rest_framework import viewsets
from api.models import Info
from api.serializers import InfoSerializer
# Create your views here.
class InfoViewSet(viewsets.ModelViewSet):
    queryset=Info.objects.all()
    serializer_class=InfoSerializer