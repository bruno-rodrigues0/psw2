from django.urls import path
from . import views

app_name = "pessoa"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("update/<int:id_pessoa>/", views.update, name="update"),
    path("delete/<int:id_pessoa>/", views.delete, name="delete"),
    path("<int:id_pessoa>/", views.details, name="details"),
]