from django.urls import path
from . import views

urlpatterns = [
    path("projects/", views.project, name="projects"),
    path("projects/<str:pk>/",views.single_project, name="project"),
    path("create-project/",views.createProject, name="create-project"),
    path('update-project/<str:pk>/',views.updateproject, name="update-project"),
    path('delete-project/<str:pk>/', views.deleteproject, name="delete-project"),

]