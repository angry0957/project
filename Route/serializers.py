from rest_framework import serializers
from . import models
from Data.models import Data


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = (
        #     'id',
        #     'title',
        #     'description',
        # )
        fields = '__all__'
        model = models.Route

    # def create(self, req, **data):
    #     print('create called')
    #     print(req, data)
    #     return super.create(self, req, data)


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        level = 2

        model = Data
