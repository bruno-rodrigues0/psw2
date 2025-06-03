from django.urls import path
from . import views

app_name = "setor"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("update/<int:id_setor>/", views.update, name="update"),
    path("delete/<int:id_setor>/", views.delete, name="delete"),
    path("<int:id_setor>/", views.details, name="details"),
]