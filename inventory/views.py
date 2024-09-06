from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ingredient, MenuItem, Purchase
from django.urls import reverse_lazy


# Create your views here.
class HomeView(TemplateView):
    template_name = "inventory/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context

class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredients_list.html"

class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = "inventory/ingredient_create.html"

class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient_update.html"

class IngredientDeleteView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = "inventory/ingredient_delete.html"
    success_url = reverse_lazy("ingredients")

class MenuItemListView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menuitems_list.html"

class MenuItemCreateView(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = "inventory/menuitem_create.html"

class MenuItemUpdateView(LoginRequiredMixin, UpdateView):
    model = MenuItem
    template_name = "inventory/menuitem_update.html"

class MenuItemDeleteView(LoginRequiredMixin, DeleteView):
    model = MenuItem
    success_url = reverse_lazy("menu")

class PurchaseListView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchases_list.html"

class PurchaseCreateView(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = "inventory/purchase_create.html"

class PurchaseUpdateView(LoginRequiredMixin, UpdateView):
    model = Purchase
    template_name = "inventory/purchase_update.html"

class PurchaseDeleteView(LoginRequiredMixin, DeleteView):
    model = Purchase
    success_url = reverse_lazy('purchases')

class ReportView(LoginRequiredMixin, TemplateView):
    template_name = "report.html"
