from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from model.group import Group


class GroupHelper:

    # конструктор класса
    def __init__(self, app):
        self.app = app

    def return_to_groups_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("group page").click()

    def open_groups_page(self):
        driver = self.app.driver
        if not (driver.current_url.endswith("/group.php") and
           len(driver.find_elements_by_name("new"))>0):
           element = WebDriverWait(driver, 60).until(
              EC.element_to_be_clickable((By.LINK_TEXT, "groups"))
           )
           element.click()
        #driver.find_element_by_link_text("groups").click()

    def create(self, group):
        self.open_groups_page()
        driver = self.app.driver
        # init group creation
        driver.find_element_by_xpath("(//input[@name='new'])[2]").click()
        self.fill_group_form(group)
        # submit group creation
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()
        self.group_cashe=None

    def fill_group_form(self, group):
        driver = self.app.driver
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        driver = self.app.driver
        if text is not None:
            driver.find_element_by_name(field_name).click()
            driver.find_element_by_name(field_name).clear()
            driver.find_element_by_name(field_name).send_keys(text)

    def delete_first_group(self):
        self.delete_group_by_index(0)
        #driver = self.app.driver
        #self.open_groups_page()
        #self.select_first_group()
        ## submit deletion
        #driver.find_element_by_name("delete").click()
        #self.return_to_groups_page()
        #self.group_cashe = None

    def delete_group_by_index(self,index):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cashe = None

    def delete_group_by_id(self, id):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion
        driver.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cashe = None

    def select_group_by_index(self,index):
        driver = self.app.driver
        driver.find_elements_by_name("selected[]")[index].click()
    def select_group_by_id(self,id):
        driver = self.app.driver
        driver.find_element_by_css_selector("input[value='%s']" % id).click()
    def select_first_group(self):
        self.select_group_by_index(0)
        #driver = self.app.driver
        #driver.find_element_by_name("selected[]").click()

    def modify_first_group(self,new_group_data):
        self.modify_group_by_index(0, new_group_data)
        #self.open_groups_page()
        #self.select_first_group()
        ## open modification form
        #driver.find_element_by_name("edit").click()
        # fill_group form
        #self.fill_group_form(new_group_data)
        ##submit modification
        #driver.find_element_by_name("update").click()
        #self.return_to_groups_page()
        #self.group_cashe = None

    def modify_group_by_index(self,index,new_group_data):
        driver = self.app.driver
        self.open_groups_page()
        #self.select_first_group()
        self.select_group_by_index(index)
        # open modification form
        driver.find_element_by_name("edit").click()
        # fill_group form
        self.fill_group_form(new_group_data)
        # submit modification
        driver.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cashe = None
    def count(self):
        driver = self.app.driver
        self.open_groups_page()
        return len(driver.find_elements_by_name("selected[]"))

    group_cashe = None
    def get_group_list(self):
        if self.group_cashe is None:
            driver = self.app.driver
            self.open_groups_page()
            self.groups=[]
            for element in driver.find_elements_by_css_selector("span.group"):
                text=element.text

                # значение атрибута value xек боксf, находящийся внутри элемета span
                id=element.find_element_by_name("selected[]").get_attribute("value")
                self.groups.append(Group(name=text,id=id))
        return list(self.groups)
