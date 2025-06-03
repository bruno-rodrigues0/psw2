from django.urls import path
from . import views

app_name = "depto"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("update/<int:id_depto>/", views.update, name="update"),
    path("delete/<int:id_depto>/", views.delete, name="delete"),
    path("<int:id_depto>/", views.details, name="details"),
]