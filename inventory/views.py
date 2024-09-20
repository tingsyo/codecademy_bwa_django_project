from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ingredient, MenuItem, Purchase, RecipeRequirement
from .forms import IngredientForm, MenuItemForm, PurchaseForm, RecipeRequirementForm
from django.urls import reverse_lazy


# Create your views here.
#@login_required(login_url="/accounts/login/")
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        context["nbar"] = "home"
        return context

class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "inventory/ingredients_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["nbar"] = "ingrdient"
        return context
    
class IngredientCreateView(LoginRequiredMixin, CreateView):
    model = Ingredient
    template_name = "inventory/ingredient_create.html"
    form_class = IngredientForm
    success_url = reverse_lazy("ingrdients")

class IngredientUpdateView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = "inventory/ingredient_update.html"
    form_class = IngredientForm
    success_url = reverse_lazy("ingrdients")

class MenuItemListView(LoginRequiredMixin, ListView):
    model = MenuItem
    template_name = "inventory/menuitems_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = MenuItem.objects.all()
        context["nbar"] = "menuitem"
        return context
    
class MenuItemCreateView(LoginRequiredMixin, CreateView):
    model = MenuItem
    template_name = "inventory/menuitem_create.html"
    form_class = MenuItemForm
    success_url = reverse_lazy("menuitem")

class PurchaseListView(LoginRequiredMixin, ListView):
    model = Purchase
    template_name = "inventory/purchases_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nbar"] = "purchase"
        return context

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
    template_name = "inventory/report.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["nbar"] = "report"
        return context

class RecipeRequirementCreateView(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    template_name = "inventory/reciperequirement_create.html"

def log_out(request):
    ''' Logout function '''
    logout(request)
    return redirect("/")