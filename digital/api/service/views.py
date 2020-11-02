from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import ServiceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Service

# Create your views here.


@api_view(['GET'])
def getAll(request):
    querySet = Service.objects.all().order_by('name')
    serializer = ServiceSerializer(querySet, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getEach(request, id):
    querySet = Service.objects.get(id=id)
    serializer = ServiceSerializer(querySet, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer = ServiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def update(request, id):
    querySet = Service.objects.get(id=id)
    serializer = ServiceSerializer(instance=querySet, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, id):
    querySet = Service.objects.get(id=id)
    querySet.delete()
    return Response('Item deleted')
