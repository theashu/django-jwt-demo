from django.shortcuts import render

from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import(
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
from .models import *
from .serializers import *
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes =  (AllowAny,)