from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('GetPlats', views.api_get_plats),
]
