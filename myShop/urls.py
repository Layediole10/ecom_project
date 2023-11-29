from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("<int:id_prod>", views.details, name="details")
]

