from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def recipes(request):
    if request.method=="POST":
        data=request.POST
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        recipe_img=request.FILES.get('recipe_img')

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_img=recipe_img,
        )
        return redirect('/recipes/')
    return render(request, "recipes.html")