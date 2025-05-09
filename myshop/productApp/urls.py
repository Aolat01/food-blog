from django.urls import path
from .views import addProductView

urlpatterns = [
    path('add-product/', addProductView, name='add-product'),
]
