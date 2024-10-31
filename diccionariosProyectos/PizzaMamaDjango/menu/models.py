from django.db import models
from django.forms import ModelForm


class Plat(models.Model):
    class PlatChoices(models.TextChoices):
        PIZZA = 'PI', 'Pizza'
        PATE = 'PA', 'Pâte'
        SALADE = 'SA', 'Salade'
        DESSERT = 'DE', 'Dessert'

    nom = models.CharField(max_length=200)
    categorie = models.CharField(
        max_length=2,
        choices=PlatChoices.choices,
        default=PlatChoices.PIZZA,
    )
    ingredients = models.CharField(max_length=400)
    prix = models.FloatField(default=0)
    vegetarienne = models.BooleanField(default=False)

    def __str__(self):
        return self.nom


class CategoriesPlatForm(ModelForm):
    class Meta:
        model = Plat
        fields = ['categorie']
