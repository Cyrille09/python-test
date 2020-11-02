from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getAll, name='get-all'),
    path('create', views.create, name='create'),
    path('get-each/<int:id>', views.getEach, name='get-each'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
