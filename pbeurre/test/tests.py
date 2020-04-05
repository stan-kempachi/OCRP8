from django.test import TestCase
from django.urls import reverse

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


# Detail Page
#     test that detail page returns a 200 if the item exists
#     test that detail page returns a 404 if the item does not exist


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
