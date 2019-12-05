from django.contrib import admin
from django.urls import path, include
from recipes.api import RecipeListAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('recipes.urls')),
    path('api/list/recipes/', RecipeListAPI.as_view()),
]
