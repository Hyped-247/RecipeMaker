from .models import Recipe
from rest_framework import viewsets, permissions
from .serializers import RecipeSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


# Recipe View set
class RecipeViewSet(viewsets.ModelViewSet):
    # queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self, *args, **kwargs):
        mo = 2
        # pk = self.request.POST.get('user')
        # user = get_object_or_404(User, pk=pk)
        # if user:
        #     return user.recipe_set.all()
        return Recipe.objects.all()

