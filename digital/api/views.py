from django.http import JsonResponse

# Create your views here.


def home(resquest):
    return JsonResponse({'info': 'django React Course', 'name': 'Cyrille Hounvio'})
