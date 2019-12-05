from django.urls import path
from rest_framework import routers
from .api import RecipeViewSet
from recipes.api import RecipeListAPI

router = routers.DefaultRouter()
router.register('api/recipes', RecipeViewSet, 'recipes')

urlpatterns = [
    path('api/list/recipes/', RecipeListAPI.as_view()),
]

urlpatterns += router.urls
