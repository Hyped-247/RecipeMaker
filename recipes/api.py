from .models import Recipe
from rest_framework import viewsets, permissions
from .serializers import RecipeSerializer


# Recipe View set
class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RecipeSerializer

    def get_queryset(self):
        return self.request.user.recipes.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
