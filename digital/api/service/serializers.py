from rest_framework import serializers
from .models import Service


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        #fields = '__all__'
        fields = ('id', 'name', 'description')
