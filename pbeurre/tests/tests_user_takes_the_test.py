from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class TestUserTakesTheTest(LiveServerTestCase):

    fixtures = ['pbeurre/fixtures/test_fixture.json']

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def submit_text_on_placeholder(self, text):
        # Wait as long as required, or maximum of 5 sec for element to appear
        # If successful, retrieves the element
        placeholder = WebDriverWait(self.driver, 5).until(
         EC.presence_of_element_located((By.ID, "searchForm")))
        placeholder.send_keys(text)
        ActionChains(self.driver).click(self.driver.find_element_by_id('button-addon2')).perform()

    # def test_user_searches(self):
    #     self.driver.get(self.live_server_url)  # L'utilisateur se rend sur la page d'acceuil
    #     self.submit_text_on_placeholder('nutella')  # Il saisit le texte dans la barre de recherche
    #     time.sleep(5)  # temps de chargement de la page
    #     self.assertIn('Vous pouvez remplacer ce produit par', self.driver.page_source)  # check the returned result

    def clicks_on_login(self):
        login_icon = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "log")))
        ActionChains(self.driver).click(login_icon).perform()

    def click_on_register(self):
        register_link = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "S'enregistrer")))
        ActionChains(self.driver).click(register_link).perform()

    def enter_logs_on_fields(self):
        username = 'Yujiro '
        email = 'yujirohanma@baki.com'
        password = 'yujiropassword'

        username_field = WebDriverWait(self.driver, 5).until(
         EC.presence_of_element_located((By.ID, "id_username")))
        self.driver.execute_script("arguments[0].click();", username_field).setAttribute("value", username)
        # username_field.send_key(username)

        self.driver.execute_script('''
            var elem = arguments[0];
            var value = arguments[1];
            elem.value = value;
        ''', username_field, username)

        # value = self.driver.execute_script('return arguments[0].value;', username_field)
        # username_field.click()
        # self.driver.execute_script("arguments[0].click();", username_field)
        # username_field.click()
        # # print(username_field)
        # username_field.send_key(username)
        # self.assertIn('Name', self.driver.page_source)
        # # username_field.send_keys(username)
        time.sleep(3)

        # email_field = WebDriverWait(self.driver, 5).until(
        #  EC.presence_of_element_located((By.CLASS_NAME, "emailLoginForm")))
        # email_field.send_keys(email)
        # password_field = WebDriverWait(self.driver, 5).until(
        #  EC.presence_of_element_located((By.CLASS_NAME, "passwordLoginForm")))
        # email_field.send_keys(password)
        # ActionChains(self.driver).click(self.driver.find_element_by_class_name('seConnecterButton')).perform()

    def test_user_register(self):
        self.driver.get(self.live_server_url)  # L'utilisateur se rend sur la page d'acceuil
        self.clicks_on_login()  # Il click sur l'icone login
        time.sleep(3)
        self.click_on_register()  # Il click sur le lien S'enregistrer
        time.sleep(3)
        self.enter_logs_on_fields()
        # assert self.driver.current_url == self.live_server_url
