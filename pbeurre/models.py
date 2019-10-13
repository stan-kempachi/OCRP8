#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models


class Category(models.Model):
    """
    Classe représentant la table 'Category' de la base de données
    """
    name = models.CharField(max_length=500, unique=True)
    picture = models.URLField(null=False)

    def __str__(self):
        return self.name


class Food(models.Model):
    """
    Classe représentant la table 'Food' de la base de données
    """
    name = models.CharField(max_length=250, unique=True)
    category = models.ManyToManyField(Category)
    category_tags1 = models.CharField(max_length=250)
    category_tags2 = models.CharField(max_length=600)
    nutri_score = models.CharField(max_length=3)
    repere_fat100g = models.CharField(max_length=3)
    repere_saturatedfat100g = models.CharField(max_length=3)
    repere_sugars100g = models.CharField(max_length=3)
    repere_saltunit = models.CharField(max_length=3)
    picture = models.URLField(null=True)
    url = models.CharField(max_length=150)
    stores = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Backup(models.Model):
    """
    Classe représentant la table 'Backup' de la base de données
    """
    food = models.ManyToManyField(Food)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.food.name


class Contact(models.Model):
    email = models.EmailField('email', max_length=100)
    name = models.CharField('nom', max_length=200)
    backup = models.OneToOneField(Backup, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


