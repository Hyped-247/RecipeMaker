from rest_framework import serializers
from .models import Recipe


# Recipe Serializer
class RecipeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Recipe
    fields = '__all__'
