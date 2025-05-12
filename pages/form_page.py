import os

from selenium.webdriver import Keys

from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators
from generator.generator import generator_person, generated_file, generator_subjects, generator_cities, generator_month_and_year

class FormPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = FormPageLocators()

    def fill_form_fields(self):
        person = next(generator_person())
        file_name, path = generated_file()
        subject = generator_subjects()
        state, city = generator_cities()
        month, month_value, year = generator_month_and_year()

        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.firstname)
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.lastname)
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)
        gender = self.element_is_visible(self.locators.GENDER)
        gender.click()
        self.element_is_visible(self.locators.MOBILE).send_keys(person.mobile)
        self.element_is_visible(self.locators.DATE_OF_BIRTH).click()
        Select(self.element_is_visible(self.locators.YEAR)).select_by_value(year)
        Select(self.element_is_visible(self.locators.MONTH)).select_by_value(month_value)
        self.element_is_visible(self.locators.DAY).click()
        self.element_is_visible(self.locators.SUBJECTS).send_keys(subject)
        self.element_is_visible(self.locators.SUBJECTS).send_keys(Keys.ENTER)
        hobbies = self.element_is_visible(self.locators.HOBBIES)
        hobbies.click()
        self.element_is_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(state)
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.ENTER)
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(city)
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.ENTER)
        self.element_is_visible(self.locators.SUBMIT).click()

        return person, gender.text, year, subject, hobbies.text, file_name, state, city

    def check_result(self):
        return [res.text for res in self.elements_are_present(self.locators.TABLE_RESULT) if res.text.strip() != '']
