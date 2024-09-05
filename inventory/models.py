from django.db import models

class Ingredient(models.Model):
    ''' An inventory of different Ingredients, their available quantity, and their prices per unit. '''
    name = models.CharField(max_length=200, unique=True)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=50, null=True)
    price_per_unit = models.FloatField(default=0.00)
    # get the absolute url
    def get_absolute_url(self):
        return "/ingredients"
    # override the default __str__ method
    def __str__(self):
        return f"""
        name={self.name};
        qty={self.quantity};
        unit={self.unit};
        unit_price={self.price_per_unit}
        """
    
class MenuItem(models.Model):
    ''' A MenuItem contains the price and recipe (a list Ingredients and their quantities). '''
    title = models.CharField(max_length=200, unique=True)
    price = models.FloatField(default=0.00)
    #
    def get_absolute_url(self):
        return "/menu"
    # Check if this MenuItem is available by checking the recipe requirements
    def available(self):
        return all(X.enough() for X in self.reciperequirement_set.all())
    # override the default __str__ method
    def __str__(self):
        return f"title={self.title}; price={self.price}"

class RecipeRequirement(models.Model):
    ''' Represents an ingredient required for a recipe for a MenuItem '''
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    # override the default __str__ method
    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; ingredient={self.ingredient.name}; qty={self.quantity}"
    #
    def get_absolute_url(self):
        return "/menu"
    # Check if this RecipeRequirement is available by checking the ingredient quantity
    def enough(self):
        return self.quantity <= self.ingredient.quantity

class Purchase(models.Model):
    """ Represents a purchase of a MenuItem """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    # override the default __str__ method
    def __str__(self):
        return f"menu_item=[{self.menu_item.__str__()}]; time={self.timestamp}"
    #
    def get_absolute_url(self):
        return "/purchases"

