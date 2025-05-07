import time
import random
import requests

from functions.base_functions import BaseFunctions

from generator.generator import generator_person
from locators.locators import TextBoxPageLocators
from locators.locators import CheckBoxPageLocators
from locators.locators import RadioButtonLocators
from locators.locators import WebTablePageLocators
from locators.locators import ButtonsPageLocators
from locators.locators import LinksPageLocators

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By



class TextBoxPage(BaseFunctions):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):

        person_info = next(generator_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_clicable(self.locators.SUBMIT).click()

        return full_name, email, current_address, permanent_address


    def check_field_form(self):

        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]

        return full_name, email, current_address, permanent_address

class CheckBoxPage(BaseFunctions):
    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:

            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.locators.TITLE_ITEM)
            data.append(title_item.text)

        return str(data).replace(' ','').replace('.doc', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)

        return str(data).replace(' ','').lower()


class RadioButtonPage(BaseFunctions):
    locators = RadioButtonLocators()

    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_RADIO_BUTTON,
                   'impressive': self.locators.IMPRESSIVE_RADIO_BUTTON,
                   'no': self.locators.NO_RADIO_BUTTON}

        self.element_is_visible(choices[choice]).click()

    def get_output_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text

class WebTablePage(BaseFunctions):
    locators = WebTablePageLocators()

    def add_new_person(self):
        count = 1
        while count != 0:
            person_info=next(generator_person())
            first_name = person_info.firstname
            last_name = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRSTNAME_INPUT).send_keys(first_name)
            self.element_is_visible(self.locators.LASTNAME_INPUT).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT).click()
            count -= 1

            return [first_name, last_name, str(age), email, str(salary), department]

    def check_new_added_person(self):
        person_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in person_list:
            if ' ' not in item.text:
                data.append(item.text.splitlines())

        return data

    def search_some_person(self, key_word):
        self.element_is_visible(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_search_person(self):
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(*self.locators.ROW_BUTTON)

        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generator_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON).click()
        self.element_is_visible(self.locators.AGE_INPUT).clear()
        self.element_is_visible(self.locators.AGE_INPUT).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT).click()

        return str(age)

    def delete_persone(self):
        self.element_is_visible(self.locators.DELETE_BUTTON).click()

    def check_deleted(self):
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    def select_up_to_some_rows(self):
        count_rows = [5, 10, 20, 25, 50, 100]
        actual_count_rows = []
        dropdown = Select(self.element_is_clicable(self.locators.COUNT_ROW_LIST))
        for option_value in count_rows:
            dropdown.select_by_value(f'{option_value}')
            actual_count_rows.append(self.check_count_rows())

        return actual_count_rows

    def check_count_rows(self):
        return len(self.elements_are_present(self.locators.FULL_PEOPLE_LIST))

class ButtonsPage(BaseFunctions):
    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click):
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_DOUBLE)
        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_on_the_button(self.locators.SUCCESS_RIGHT)
        if type_click == "click":
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_on_the_button(self.locators.SUCCESS_CLICK_ME)

    def check_clicked_on_the_button(self, element):
        return self.element_is_visible(element).text

class LinksPage(BaseFunctions):
    locators = LinksPageLocators()

    def check_home_link(self):
        simple_link = self.element_is_visible(self.locators.HOME_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.switch_to_new_tab()
            url = self.driver.current_url
            return link_href, url
        else:
            return link_href, request.status_code

    def check_created_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.CREATED_LINK).click()
        else:
            return request.status_code

    def check_no_content_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.NO_CONTENT_LINK).click()
        else:
            return request.status_code

    def check_moved_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.MOVED_LINK).click()
        else:
            return request.status_code


    def check_bad_request_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST_LINK).click()
        else:
            return request.status_code

    def check_unauthorized_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.UNAUTHORIZED_LINK).click()
        else:
            return request.status_code

    def check_forbidden_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.FORBIDDEN_LINK).click()
        else:
            return request.status_code

    def check_not_found_link(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.NOT_FOUND_LINK).click()
        else:
            return request.status_code