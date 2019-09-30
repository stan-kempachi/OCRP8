#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import django
import django.db
import psycopg2.errors
from constantes import *

django.setup()

# import personnal module
from pbeurre import models
import classes as cl


try:
    conn = psycopg2.connect(user="stan",
                            password="",
                            host="127.0.0.1",
                            port="5432",
                            database="pbeurre")

    cursor = conn.cursor()
    # Print PostgreSQL Connection properties
    print(conn.get_dsn_parameters(), "\n")
    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")
except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)





def recup_data_api(url):
    """Take an url and return data"""
    data = requests.get(url)
    data.encoding = "utf8"
    return data.json()


def load_category():
    models.Category.objects.all().delete()
    url = "https://fr.openfoodfacts.org/categories/.json"
    data_from_url = recup_data_api(url)
    print("Lancement de la récupération des catégories . Allez on patiente un peu ! ")
    for elt in name_list:
        for data in data_from_url["tags"]:
            if data["name"] == elt:
                categories.append(data["url"])
                try:
                    data_from_cat = recup_data_api(data["url"] + (str("/.json")))
                    for data in data_from_cat["products"]:
                        try:
                            category = cl.Categories(data)
                            models.Category.objects.create(name=elt, picture=category.picture)
                        except (django.db.utils.IntegrityError, django.db.utils.DataError, AttributeError):
                            pass
                except(django.db.utils.IntegrityError, django.db.utils.DataError):
                    print("Catégories : __{}__ non récupérés !".format(data["url"]))
                    pass
        else:
            pass


def lister_url():
    print("Récupération des produits en cours")
    for elt in categories:
        for i in range(1, 40):  # generation d'une boucle
            urls_list.append('{0}/{1}.json'.format(elt, str(i)))  # ajout à nouvelle liste


def load_product():
    models.Food.objects.all().delete()
    for url in urls_list:
        print(url)
        data_from_list = recup_data_api(url)
        for data in data_from_list["products"]:
            if "en:" in data["categories"]:  # On ne prend pas celles en anglais
                pass
            else:
                for category_name in name_list:
                    if category_name in data["categories"]:
                        try:
                            food = cl.Food(data)
                            models.Food.objects.create(name=food.name,
                                                       category_tags1=category_name,
                                                       category_tags2=food.category_tags2,
                                                       nutri_score=food.nutri_score,
                                                       repere_fat100g=food.repere_fat100g,
                                                       repere_saltunit=food.repere_saltvalue,
                                                       repere_sugars100g=food.repere_sugars100g,
                                                       repere_saturatedfat100g=food.repere_saturatedfat100g,
                                                       picture=food.picture,
                                                       url=food.url,
                                                       stores=food.stores)
                        except(django.db.utils.IntegrityError, django.db.utils.DataError, AttributeError):
                            try:
                                print("Ce produit n'a put être récupéré:  {}".format(food.name))
                            except AttributeError:
                                pass

                            pass
                    else:
                        pass
    print("Récupération terminée")



def main():
    """Main function, lauching the script"""
    # Call the sql script to create the database
    print("Initialisation du chargement de la base de données pbeurre !")
    load_category()
    print("Catégories entièrements chargées")
    lister_url()
    print("Chargement des produits en cours... On se détend , un café ? ")
    load_product()
    print("Base de données pbeurre chargé avec succès !")


if __name__ == "__main__":
    main()
