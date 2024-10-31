from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('pizzas', views.pizzas, name="pizzas"),
    path('salades', views.salades, name="salades"),
    path('pates', views.pates, name="pâtes"),
    path('desserts', views.desserts, name="desserts"),
]
