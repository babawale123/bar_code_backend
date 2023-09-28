from django.shortcuts import render
from rest_framework import viewsets
from .serializer import EventSerializer, Event

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer