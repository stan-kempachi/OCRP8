#!/usr/bin/env python
# -*- coding: utf-8 -*-

import django
django.setup()

import requests
import django.db

# import personnal module
from pbeurre.management.commands._constantes import name_list, urls_list, categories
from pbeurre.models import Food, Category
from pbeurre.management.commands import _classes as cl


def drop_everythings():
    Category.objects.all().delete()
    Food.objects.all().delete()


def get_data(url):
    """Take an url and return data"""
    data = requests.get(url)
    data.encoding = "utf8"
    return data.json()


def load_category():
    url = "https://fr.openfoodfacts.org/categories/.json"
    data_from_url = get_data(url)
    print("Lancement de la récupération des catégories . Allez on patiente un peu ! ")
    for elt in name_list:
        for data in data_from_url["tags"]:
            if data["name"] == elt:
                categories.append(data["url"])
                try:
                    data_from_cat = get_data(data["url"] + (str("/.json")))
                    for dat in data_from_cat["products"]:
                        try:
                            category = cl.Categories(dat)
                            cat = Category(name=elt, picture=category.picture)
                            cat.save()
                            print(cat.name)
                        except (django.db.utils.IntegrityError, django.db.utils.DataError, AttributeError):
                            pass
                except(django.db.utils.IntegrityError, django.db.utils.DataError):
                    print("Catégories : __{}__ non récupérés !".format(data["url"]))
                    pass
        else:
            pass


def list_url():
    print("Récupération des produits en cours")
    for elt in categories:
        for i in range(1, 40):  # generation d'une boucle
            urls_list.append('{0}/{1}.json'.format(elt, str(i)))  # ajout à nouvelle liste


def load_product():
    for url in urls_list:
        print(url)
        data_from_list = get_data(url)
        for data in data_from_list["products"]:
            if "en:" in data["categories"]:  # On ne prend pas celles en anglais
                pass
            else:
                for category_name in name_list:
                    if category_name in data["categories"]:
                        try:
                            food = cl.Food(data)
                            cat = Category.objects.get(name=category_name)
                            foo = Food(name=food.name,
                                       category=cat,
                                       category_tags2=food.category_tags2,
                                       nutri_score=food.nutri_score,
                                       repere_fat100g=food.repere_fat100g,
                                       repere_saltunit=food.repere_saltvalue,
                                       repere_sugars100g=food.repere_sugars100g,
                                       repere_saturatedfat100g=food.repere_saturatedfat100g,
                                       picture=food.picture,
                                       url=food.url,
                                       stores=food.stores)
                            foo.save()
                        except(django.db.utils.IntegrityError, django.db.utils.DataError, AttributeError,
                               Category.DoesNotExist):
                            try:
                                print("Ce produit n'a put être récupéré:  {}".format(food.name))
                            except AttributeError:
                                pass
                    else:
                        pass
    print("Récupération terminée")

