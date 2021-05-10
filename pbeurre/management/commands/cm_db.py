from django.core.management.base import BaseCommand
from pbeurre.management.commands._load_db import drop_everythings, load_category, list_url, load_product
import psycopg2.errors


class Command(BaseCommand):
    help = 'Load the database'

    def handle(self, **options):
        try:
            conn = psycopg2.connect(user="Stan",
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
        drop_everythings()
        print("Initialisation du chargement de la base de données pbeurre !")
        load_category()
        print("Catégories entièrements chargées")
        list_url()
        print("Chargement des produits en cours... On se détend , un café ? ")
        load_product()
        print("Base de données pbeurre chargé avec succès !")

