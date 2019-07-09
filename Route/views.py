from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from Route import models
from . import serializers
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views import View
from django.http import HttpResponse
from rest_framework.views import APIView, Response


class RouteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer


class DataViewSet(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request):
        return HttpResponse('result')

        # return render(request, 'data.html')
