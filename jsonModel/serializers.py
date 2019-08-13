from rest_framework import serializers
from . import models


class JsonModelSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.JsonModel
