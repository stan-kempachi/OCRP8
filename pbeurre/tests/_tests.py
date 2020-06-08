
from django.test import TestCase
from django.urls import reverse


from pbeurre.models import Food, Category, Backup
from django.contrib.auth.models import User


# Index page
class IndexPageTestCase(TestCase):

    # test the index page return a 200
    def test_index_page(self):
        response = self.client.get(reverse('pbeurre:index'))
        self.assertEqual(response.status_code, 200)


# Mention Legal page
class MentionLegalPageTestCase(TestCase):

    # test the mention legal page return a 200
    def test_mention_page(self):
        response = self.client.get(reverse('pbeurre:mention'))
        self.assertEqual(response.status_code, 200)


# Search Page
class SearchPageTestCase(TestCase):

    # database test values
    def setUp(self):
        self.category_mushrooms = Category.objects.create(name='mushrooms')
        self.magic_food = Food.objects.create(name='magic food', category=self.category_mushrooms, nutri_score='a')
        self.epic_food = Food.objects.create(name='epic food', category=self.category_mushrooms, nutri_score='a')

    # test return if the search is valid
    def test_search_page_returns_200_if_food_found(self):
        query = self.epic_food.name
        response = self.client.get(reverse('pbeurre:search'), {'q': query})
        self.assertEqual(response.status_code, 200)

    # test return 404 if the search is not valid
    def test_search_page_returns_404_if_not_food_found(self):
        query = 'faux_nom_qui_ne_sera_jamais_trouvé'
        response = self.client.get(reverse('pbeurre:search'), {'q': query})
        self.assertEqual(response.status_code, 404)

    # test pagination is active
    def test_search_page_returns_true_pagination_number(self):
        query = self.epic_food.name
        response = self.client.get(reverse('pbeurre:search'), {'q': query})
        self.assertEqual(response.context['paginate'], True)


# Details Page
class DetailsPageTestCase(TestCase):

    # database test values
    def setUp(self):
        self.category_mushrooms = Category.objects.create(name='mushrooms')
        self.magic_food = Food.objects.create(name='magic food', category=self.category_mushrooms)

    # test that detail page returns a 200 if the item exists
    def test_details_page_returns_200(self):
        response = self.client.get(reverse('pbeurre:details', args=(self.magic_food.id,)))
        self.assertEqual(response.status_code, 200)

    # # test that detail page returns a 404 if the item does not exist
    def test_details_page_returns_404(self):
        fake_id = self.magic_food.id + 1
        response = self.client.get(reverse('pbeurre:details', args=(fake_id,)))
        self.assertEqual(response.status_code, 404)


# Register Page
class RegisterPageTestCase(TestCase):

    # test register a new user
    def test_new_user_registered(self):
        old_users = User.objects.count()
        password = 'Testpassword'
        user = User.objects.create(username='Regis', email='register@test.com')
        user.set_password(password)
        user.save()
        username = user.username
        email = user.email
        password = user.password
        self.client.post(reverse('pbeurre:register'), {
            'name': username,
            'email': email,
            'password': password
        })
        new_users = User.objects.count()
        self.assertEqual(new_users, old_users + 1)


# Login Page
class LoginPageTestCase(TestCase):

    # database test values
    def setUp(self):
        self.user = User.objects.create(username='Saitama', email='saitama@one.punch')
        self.user.set_password('testpassword')
        self.user.save()

    # test if login page authenticated user
    def test_login(self):
        response = self.client.post(reverse('pbeurre:login'), {
            'username': self.user.username,
            'password': 'testpassword'
        }, follow=True)
        self.client.login(username=self.user.username, password=self.user.password)
        self.assertTrue(response.context['user'].is_authenticated)

    # test if login page return Anonymous with fake user
    def test_login_fake_user(self):
        response = self.client.post(reverse('pbeurre:login'), {
            'username': 'Fake_user',
            'password': 'fakepassword'
        }, follow=True)
        self.client.login(username='Fake_user', password='fakepassword')
        self.assertTrue(response.context['user'].is_anonymous)


# Logout Page
class LogoutPageTestCase(TestCase):

    # database test values
    def setUp(self):
        self.user = User.objects.create(username='Kisuke ', email='urahara.kisuke@bleach.soul')
        self.user.set_password('kisukepassword')
        self.user.save()

    # test if logout page return anonyme user
    def test_logout(self):
        self.client.post(reverse('pbeurre:login'), {
            'username': self.user.username,
            'password': 'kisukepassword'
        }, follow=True)
        self.client.login(username=self.user.username, password=self.user.password)
        response = self.client.post(reverse('pbeurre:logout'), follow=True)
        self.client.logout()
        self.assertTrue(response.context['user'].is_anonymous)


# Backup Page
class BackupPageTestCase(TestCase):

    # database test values
    def setUp(self):
        self.user = User.objects.create(username='Gin ', email='ichimaru.gin@bleach.soul')
        self.user.set_password('ginpassword')
        self.user.save()
        Category.objects.create(name='mushrooms')
        self.category_mushrooms = Category.objects.get(name='mushrooms')
        Food.objects.create(id='1', name='magic food', category=self.category_mushrooms)
        self.magic_food = Food.objects.get(name='magic food')

    # test to add a new backup if user logged
    def test_new_backup_logged_user(self):
        food_id = self.magic_food.id
        old_backup = Food.objects.filter(backup__user_id=self.user).count()
        self.client.force_login(self.user)
        self.client.get(reverse('pbeurre:add_favorite', args=(food_id,)))
        new_backup = Food.objects.filter(backup__user_id=self.user).count()
        self.assertEqual(new_backup, old_backup + 1)

    # test no add a food already on backup
    def test_no_add_food_already_on_backup_(self):
        food = Food.objects.filter(name=self.magic_food.name)
        backup = Backup.objects.create(user_id=self.user.id)
        backup.food.set(food)
        old_backup = Food.objects.filter(backup__user_id=self.user).count()
        self.client.force_login(self.user)
        self.client.get(reverse('pbeurre:add_favorite', args=(self.magic_food.id,)))
        new_backup = Food.objects.filter(backup__user_id=self.user).count()
        self.assertEqual(new_backup, old_backup)

    # test to add a new backup if user not logged is redirected to login
    def test_new_backup_user_not_logged(self):
        food_id = self.magic_food.id
        response = self.client.get(reverse('pbeurre:add_favorite', args=(food_id,)))
        self.assertRedirects(response, '/pbeurre/login/?next=/pbeurre/addfavorite/1/')

    # test if a backup belongs to a contact
    def test_a_backup_belongs_to_contact(self):
        food_id = self.magic_food.id
        self.client.force_login(self.user)
        self.client.get(reverse('pbeurre:add_favorite', args=(food_id,)))
        backup = Backup.objects.first()
        self.assertEqual(self.user.username, backup.user.username)

    # test that a backup belongs to a food
    def test_a_backup_belongs_to_food(self):
        food_id = self.magic_food.id
        self.client.force_login(self.user)
        self.client.get(reverse('pbeurre:add_favorite', args=(food_id,)))
        backup = Food.objects.get(backup__user_id=self.user.id)
        self.assertEqual(food_id, backup.id)


# favorite page
class FavoritePageTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Zaraki ', email='zaraki.kempachi@bleach.soul')
        self.user.set_password('zarakipassword')
        self.user.save()

    # test favorite page redirect to login not logged users
    def test_favorite_page_redirect_to_login_not_logged_users(self):
        response = self.client.get(reverse('pbeurre:favorite'))
        self.assertRedirects(response, '/pbeurre/login/?next=/pbeurre/favorite/')

    # test favorite page return 200 for logged users
    def test_fav_page_return_200(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('pbeurre:favorite'))
        self.assertEqual(response.status_code, 200)
