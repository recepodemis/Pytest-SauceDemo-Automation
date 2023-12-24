from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.keys import Keys
import pytest

class Test_Sauce_Optioanl:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()
    
    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_checkToCard(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.ENTER)
        clickItem = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")))
        clickItem.click()
        clickCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='shopping_cart_container']/a")))
        clickCart.click()
        checkItem = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='item_4_title_link']/div")))
        assert checkItem.text == "Sauce Labs Backpack"

    @pytest.mark.xfail
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_checkToCardRemoved(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.ENTER)
        addItem = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")))
        addItem.click()
        clickCart = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='shopping_cart_container']/a")))
        clickCart.click()
        removeItem =  WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"remove-sauce-labs-backpack")))
        removeItem.click()
        continueShopping =  WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"continue-shopping")))
        continueShopping.click()
        clickCart.click()
        checkItem = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='item_4_title_link']/div")))
        assert checkItem.text == "Sauce Labs Backpack"

    @pytest.mark.parametrize("username,password",[("recepodemis","deneme"),("testrecep","secret_sauce"),("standard_user","test_password")])
    def test_failedLogin(self,username,password):
        usernameInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys(username)
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys(password)
        passwordInput.send_keys(Keys.ENTER)
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
