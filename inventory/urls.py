from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('ingredient/', views.HomeView.as_view(), name='ingredients'),
    path('menuitem/', views.HomeView.as_view(), name='menu'),
    path('purchase/', views.HomeView.as_view(), name='purchases'),
    path('report/', views.HomeView.as_view(), name='reports'),
]
