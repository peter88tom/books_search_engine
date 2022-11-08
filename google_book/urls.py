from django.urls import path
from google_book import views

urlpatterns = [
    path('', views.index),
]
