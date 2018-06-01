#from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from fixture.session import SessionHelper
class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)
        self.session=SessionHelper(self) # помощник получает ссылку на объект
                                         # класса Application



    def open_home_page(self):
        driver = self.driver
        driver.get('http://localhost/addressbook')


    def return_to_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("group page").click()

    def open_groups_page(self):
        driver = self.driver
        driver.find_element_by_link_text("groups").click()

    def create_group(self, group):
        driver = self.driver
        self.open_groups_page()
        # init group creation
        driver.find_element_by_xpath("(//input[@name='new'])[2]").click()
        # fill group form
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def destroy(self):
        self.driver.quit()
