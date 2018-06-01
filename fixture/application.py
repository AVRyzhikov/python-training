#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)

        self.session=SessionHelper(self) # помощник получает ссылку на объект
                                         # класса Application
        self.group = GroupHelper(self)



    def open_home_page(self):
        driver = self.driver
        driver.get('http://localhost/addressbook')




    def destroy(self):
        self.driver.quit()
