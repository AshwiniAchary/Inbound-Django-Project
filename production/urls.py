from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_receipt, name='create_receipt'),
    path('pallet_list/', views.pallet_list, name='pallet_list'),
]
