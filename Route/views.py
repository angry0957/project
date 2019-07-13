from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from Route import models
from Data.models import Data
from . import serializers
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class RouteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer


class DataViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    queryset = Data.objects.all()
    serializer_class = serializers.DataSerializer
