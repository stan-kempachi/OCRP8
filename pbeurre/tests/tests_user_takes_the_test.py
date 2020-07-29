from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager



class TestUserTakesTheTest(LiveServerTestCase):

    fixtures = ['pbeurre/fixtures/test_fixture.json']

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def submit_text_on_placeholder(self, text):
        # Wait as long as required, or maximum of 5 sec for element to appear
        # If successful, retrieves the element
        placeholder = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "searchForm")))
        placeholder.send_keys(text)
        ActionChains(self.driver).click(self.driver.find_element_by_id('button-addon2')).perform()

    def clicks_on_login(self):
        login_icon = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "log")))
        ActionChains(self.driver).click(login_icon).perform()

    def clicks_on_save(self):
        add_icon = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located((By.ID, "favbouton")))
        add_icon[0].click()

    def click_on_backup(self):
        fav_ico = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "carot")))
        fav_ico.click()

    def enter_text_on_login_fields(self):
        username = 'Stan'
        password = 'Stanpassword'
        username_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "email")))
        username_field.send_keys(username)
        password_add = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "id_password")))
        password_add.send_keys(password)
        time.sleep(3)
        ActionChains(self.driver).click(self.driver.find_element_by_class_name('seConnecterButton')).perform()

    def enter_logs_on_fields(self):
        username = 'Yujiro'
        email = 'yujirohanma@baki.com'
        password = 'yujiropassword'
        username_add = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Name']")))
        username_add.send_keys(username)
        email_add = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Email']")))
        email_add.send_keys(email)
        password_add = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']")))
        password_add.send_keys(password)
        time.sleep(3)
        ActionChains(self.driver).click(self.driver.find_element_by_class_name('seConnecterButton')).perform()

    def click_on_register(self):
        register_link = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, "S'enregistrer")))
        ActionChains(self.driver).click(register_link).perform()

    def test_user_searches(self):
        self.driver.get(self.live_server_url)  # L'utilisateur se rend sur la page d'acceuil
        self.submit_text_on_placeholder('nutella')  # Il saisit le texte dans la barre de recherche
        time.sleep(5)  # temps de chargement de la page
        assert 'Vous pouvez remplacer ce produit par' in self.driver.page_source  # check the returned result

    def test_user_login(self):
        self.driver.get(self.live_server_url)  # L'utilisateur se rend sur la page d'acceuil
        self.clicks_on_login()  # Il click sur l'icone login
        self.enter_text_on_login_fields()
        time.sleep(3)
        assert 'Du gras, oui, mais de qualite!' in self.driver.page_source

    def test_user_register(self):
        self.driver.get(self.live_server_url)  # L'utilisateur se rend sur la page d'acceuil
        self.clicks_on_login()  # Il click sur l'icone login
        time.sleep(3)
        self.click_on_register()  # Il click sur le lien S'enregistrer
        time.sleep(3)
        self.enter_logs_on_fields()
        time.sleep(3)
        assert 'Du gras, oui, mais de qualite!' in self.driver.page_source

    def test_user_add_backup(self):
        self.driver.get(self.live_server_url)  # L'utilisateur se rend sur la page d'acceuil
        self.clicks_on_login()
        time.sleep(3)  # temps de chargement de la page
        self.enter_text_on_login_fields()
        time.sleep(3)  # temps de chargement de la page
        self.submit_text_on_placeholder('nutella')  # Il saisit le texte dans la barre de recherche
        time.sleep(3)  # temps de chargement de la page
        self.clicks_on_save()
        time.sleep(3)  # temps de chargement de la page
        assert 'Vos Produits Favoris :' in self.driver.page_source

    def test_user_acces_to_backup(self):
        self.driver.get(self.live_server_url)  # L'utilisateur se rend sur la page d'acceuil
        time.sleep(3)  # temps de chargement de la page
        self.clicks_on_login()
        time.sleep(3)  # temps de chargement de la page
        self.enter_text_on_login_fields()
        time.sleep(3)  # temps de chargement de la page
        self.click_on_backup()
        time.sleep(3)  # temps de chargement de la page
        assert 'Vos Produits Favoris :' in self.driver.page_source
