from rest_framework import routers
from django.urls import path, include

from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    path('login/', obtain_auth_token, name='signin'),
    path('logout/<int:id>/', views.signout, name='signout'),
    path('', include(router.urls)),
    path('each/<int:id>', views.getEach, name='each'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),

]
