#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Ce fichier contient des classes représentant la base de données de ce programme"""


class Categories():
    """Classe représentant la table 'Categories' de la base de données"""

    def __init__(self, data_from_off, index=None):
        """Initier un dictionnaire pour argument"""
        # Utiliser la clé lors de la création de la base de données à partir de l'API OFF
        try:
            self.id = data_from_off["id"]
            self.name = data_from_off["categories"]
            self.picture = data_from_off["image_url"]
        except KeyError:
            pass
        # Utilisez l'index lorsque l'on appel la classe depuis le programme
        except TypeError:
            self.name = data_from_off
            self.index = index


class Food():
    """Classe représentant la table 'Food' de la base de données"""

    def __init__(self, data_from_off, index=None):
        """Initier un dictionnaire pour argument"""

        # Utiliser la clé lors de la création de la base de données à partir de l'API OFF
        try:
            self.name = data_from_off["product_name_fr"]
            pass
            try:
                self.category = data_from_off["categories"].split(",")
            except KeyError:
                pass
            try:
                self.nutri_score = data_from_off["nutrition_grade_fr"]
            except KeyError:
                pass
            try:
                self.repere_100g = {(data_from_off["nutriments"]["fat_100g"]) + (data_from_off["nutriments"]["salt_unit"])\
                + (data_from_off["nutriments"]["saturated-fat_100g"]) + (data_from_off["nutriments"]["sugars_100g"])}
            except KeyError:
                self.repere_100g = "None"
            try:
                self.picture = data_from_off["image_url"]
            except KeyError:
                pass
            try:
                self.stores = data_from_off["stores"]
            except KeyError:
                self.stores = "None"
            try:
                self.url = data_from_off["url"]
            except KeyError:
                self.url = "Url not available"
        except KeyError:
            pass
        except IndexError:
            pass
        except TypeError:
            self.id = data_from_off
            self.tags = data_from_off
            self.nutri_score = data_from_off
            self.repere_100g = data_from_off["nutriments"]
            self.picture = data_from_off
            self.stores = ""
            try:
                self.stores = data_from_off
            except IndexError:
                pass
            try:
                self.url = data_from_off
            except IndexError:
                self.url = data_from_off
            self.index = index

