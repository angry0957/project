from rest_framework import serializers
from . import models


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = (
        #     'id',
        #     'title',
        #     'description',
        # )
        fields = '__all__'
        model = models.Route
