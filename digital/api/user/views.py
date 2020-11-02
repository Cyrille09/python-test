from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import login, logout
import random
import re
# Create your views here.


def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]) for _ in range(length))


@api_view(['GET'])
def getAll(request):
    querySet = CustomUser.objects.all().order_by('name')
    serializer = UserSerializer(querySet, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getEach(request, id):
    querySet = CustomUser.objects.get(id=id)
    serializer = UserSerializer(querySet, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def update(request, id):
    querySet = CustomUser.objects.get(id=id)
    serializer = UserSerializer(instance=querySet, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete(request, id):
    querySet = CustomUser.objects.get(id=id)
    querySet.delete()
    return Response('Item deleted')


@api_view(['GET'])
def signout(request, id):
    logout(request)

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = ""
        user.save()

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid user ID'})

    return JsonResponse({'success': 'Logout success'})


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}

    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]

        except KeyError:
            return [permission() for permission in self.permission_classes]
