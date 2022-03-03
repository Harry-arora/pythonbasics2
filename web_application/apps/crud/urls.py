from django.urls import path, include
from apps.crud import views

urlpatterns = [
    path('hello/', views.hello),
    path('hey/', views.hey),
    path('tutorial_put', views.tutorial_put),
    path('tutorial_list_published', views.tutorial_list_published),
    path('tutorial_delete', views.tutorial_delete),
    path('single_project', views.single_project),
]