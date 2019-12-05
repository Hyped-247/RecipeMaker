from rest_framework import viewsets, permissions, generics
from recipes.models import Recipe
from .serializers import RecipeSerializer


# Recipe View set
class RecipeViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RecipeSerializer

    def get_queryset(self):
        return self.request.user.recipe_set.all()


# Recipe List API
class RecipeListAPI(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
