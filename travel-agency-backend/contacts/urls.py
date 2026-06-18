from django.urls import path
from .views import *

urlpatterns = [
    path('', ContactListCreateView.as_view()),
    path('<int:pk>/', ContactDetailView.as_view()),
]
