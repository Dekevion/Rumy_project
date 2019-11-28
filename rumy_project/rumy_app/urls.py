from rest_framework import routers
from .models import UserModel
from .api import UserViewSet
from django.urls import path, include
from . import views

router = routers.DefaultRouter()

router.register('user',UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('user_verify/',views.client_to_server,name='verify')
]