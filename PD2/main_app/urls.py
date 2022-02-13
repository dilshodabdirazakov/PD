from django.urls import path
from .views import index
from .views import board

urlpatterns = [
    path('', index, name='index'),
    path('board/', board, name='board'),
]