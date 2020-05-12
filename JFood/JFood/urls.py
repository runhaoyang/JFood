from django.urls import path
from . import views
from .views import RecipeArticleView, AddRecipeView, UpdateRecipeView

urlpatterns = [
    path('', views.index, name = "index"),
    path('register/', views.register, name = "register"),
    path('recipes/<int:pk>', RecipeArticleView.as_view(), name = "recipe-detail"),
    path('addrecipe/', AddRecipeView.as_view(), name = "add_recipe"),
    path('recipes/', views.recipes, name ="recipes"),
    path('searchrecipe/', views.searchRecipe, name="searchRecipe"),
    path('updaterecipe/<int:pk>', UpdateRecipeView.as_view(), name = 'updaterecipe'),
]