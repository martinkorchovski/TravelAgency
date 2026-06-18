from django.urls import path
from .views import *

urlpatterns = [
    path('', destination_list),
    path('<int:pk>/', destination_details),
]

