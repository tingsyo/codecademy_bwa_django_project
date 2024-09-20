from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("logout/", views.log_out, name="logout"),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path('', views.HomeView.as_view(), name='home'),
    path('ingredient/', views.IngredientListView.as_view(), name='ingredients'),
    path('ingredient/create', views.IngredientCreateView.as_view(), name="create_ingredient"),
    path('ingredient/<slug:pk>/update', views.IngredientUpdateView.as_view(), name="update_ingredient"),
    path('menuitem/', views.MenuItemListView.as_view(), name='menuitem'),
    path('menuitem/create', views.MenuItemCreateView.as_view(), name="create_menuitem"),
    path('purchase/', views.PurchaseListView.as_view(), name='purchases'),
    path('report/', views.ReportView.as_view(), name='reports'),
]
