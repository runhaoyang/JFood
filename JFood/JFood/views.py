from django.shortcuts import render
from .models import Recipe
from django.views.generic import DetailView, CreateView, UpdateView



dests = Recipe.objects.all()
# Create your views here.
def index(request):
    return render(request, "index.html", {'dests' : dests})

def register(request):
    return render(request, 'register.html' )

def recipes(request):
    return render(request, 'recipes.html', {'dests' : dests})

def searchRecipe(request):
    search = request.POST.get('search')
    print(search)
    send = {
        'search': search,
        'dests' : dests
    }
    return render(request, 'searchrecipe.html', send)

class RecipeArticleView(DetailView):
    model = Recipe
    template_name = 'recipe-details.html'

class AddRecipeView(CreateView):
    model = Recipe
    template_name = 'add_recipe.html'
    #fields = '__all__'
    fields = ('name', 'img', 'author', 'ingredients', 'cookingDirections')

class UpdateRecipeView(UpdateView):
    model = Recipe
    template_name = 'update_recipe.html'
    fields = ['name', 'img', 'author', 'ingredients', 'cookingDirections']

