
from django.test import TestCase
from django.urls import reverse
from pbeurre.models import Food, Category
from django.shortcuts import get_object_or_404


# open the index page
# writing a search
# click on search
# open the search page
# (click on details)
# click on add to favorite
# login page
# favorite page


# Index page
class IndexPageTestCase(TestCase):
    # test the index page return a 200
    def test_index_page(self):
        reponse = self.client.get(reverse('index'))
        self.assertEqual(reponse.status_code, 200)


# Mention Legal page
class MentionLegalPageTestCase(TestCase):
    # test the mention legal page return a 200
    def test_mention_page(self):
        reponse = self.client.get(reverse('mention'))
        self.assertEqual(reponse.status_code, 200)


# Details Page
class DetailsPageTestCase(TestCase):
    # test that detail page returns a 200 if the item exists
    def test_details_page_returns_200(self):
        category = Category.objects.create(name='mushrooms')
        category_mushrooms = Category.objects.get(name='mushrooms')
        magicfood = Food.objects.create(name='magic food', category=category_mushrooms)
        magicfood_id = Food.objects.get(name='magic food').id
        reponse = self.client.get(reverse('pbeurre:details', args=(magicfood_id,)))
        self.assertEqual(reponse.status_code, 200)

    # # test that detail page returns a 404 if the item does not exist
    def test_details_page_returns_404(self):
        category = Category.objects.create(name='awesome cat name')
        category_awesome = Category.objects.get(name='awesome cat name')
        food = Food.objects.create(name='foodname', category=category_awesome)
        food_id = Food.objects.get(name='foodname').id + 1
        reponse = self.client.get(reverse('pbeurre:details', args=(food_id,)))
        self.assertEqual(reponse.status_code, 404)


# Login Page
#   test if login page returns a 200
#   test user logged in if the items are valid


# Backup Page
#     test that a new backup is made
#     test that a backup belongs to a contact
#     test that a food already on backup

# Search Page
#     test return 404 if the search is not valid
#     test return the correct page number of pagination
