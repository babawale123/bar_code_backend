from django.urls import path, include
from .views import EventViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('events', EventViewSet)
urlpatterns =[
    path('', include(router.urls))
]