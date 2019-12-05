from django.db import models
from recipes.models import Recipe


class Step(models.Model):
    step_text = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.step_text
