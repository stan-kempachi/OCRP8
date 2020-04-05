from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Classe représentant la table 'Category' de la base de données
    """
    name = models.CharField('nom', max_length=500, unique=True)
    picture = models.URLField('image', null=False)

    class Meta:
        verbose_name = "categorie"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Food(models.Model):
    """
    Classe représentant la table 'Food' de la base de données
    """
    name = models.CharField('nom', max_length=250, unique=True)
    category = models.ManyToManyField(Category)
    category_tags1 = models.CharField('category_tags1', max_length=250)
    category_tags2 = models.CharField('category_tags2', max_length=600)
    nutri_score = models.CharField('nutri_score', max_length=3)
    repere_fat100g = models.CharField(max_length=3)
    repere_saturatedfat100g = models.CharField(max_length=3)
    repere_sugars100g = models.CharField(max_length=3)
    repere_saltunit = models.CharField(max_length=3)
    picture = models.URLField('image', null=True)
    url = models.CharField('lien', max_length=150)
    stores = models.CharField('magasin', max_length=250)

    class Meta:
        verbose_name = "aliment"
        verbose_name_plural = "aliments"

    def __str__(self):
        return self.name


class Backup(models.Model):
    """
    Classe représentant la table 'Backup' de la base de données
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    food = models.ManyToManyField(Food)

    class Meta:
        verbose_name = "favori"
        verbose_name_plural = "favoris"

    def __str__(self):
        return self.user.username
