import random
import time

from data.data import color_list

from selenium.webdriver.support.wait import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC

from selenium.common import TimeoutException
from selenium.webdriver import Keys, ActionChains

from locators.widgets_locators import WidgetsPageLocators
from locators.widgets_locators import AutoCompletePageLocators
from pages.base_page import BasePage


class WidgetsPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = WidgetsPageLocators()

    def check_accordian(self, accordian_num):
        section_dict = {
            'first': {'title': self.locators.SECTION_FIRST,
                      'content': self.locators.SECTION_CONTENT_FIRST},
            'second': {'title': self.locators.SECTION_SECOND,
                       'content': self.locators.SECTION_CONTENT_SECOND},
            'third': {'title': self.locators.SECTION_THIRD,
                      'content': self.locators.SECTION_CONTENT_THIRD}
        }

        section_title = self.element_is_clickable(section_dict[accordian_num]['title'])
        section_title.click()
        section_content = self.element_is_visible(section_dict[accordian_num]['content'])

        return section_title.text, section_content.text


class AutoCompletePage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = AutoCompletePageLocators()

    def check_fill_input_multi(self):
        colors = random.sample(color_list, random.randint(2, len(color_list)))
        input_multi = self.element_is_visible(self.locators.MULTI_INPUT)

        for color in colors:
            input_multi.send_keys(color)
            ActionChains(self.driver).pause(0.1).perform()
            input_multi.send_keys(Keys.ENTER)

        chosen_colors, count_colors_before, count_colors_after = self.get_colores_input_multi()

        return colors, chosen_colors, count_colors_before, count_colors_after

    def remove_colores_from_multi(self):
        remove_button_list = self.elements_are_present(self.locators.MULTI_VALUE_REMOVE)
        for color in remove_button_list:
            color.click()
            break

    def get_colores_input_multi(self):
        count_colors_before = self.elements_are_present(self.locators.MULTI_VALUE)
        chosen_colors = [color.text for color in count_colors_before]
        self.remove_colores_from_multi()
        count_colors_after = self.elements_are_present(self.locators.MULTI_VALUE)
        return chosen_colors, len(count_colors_before), len(count_colors_after)

    def check_fill_input_single(self):
        color = random.choice(color_list)
        input_single = self.element_is_visible(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        chosen_color = self.element_is_present(self.locators.SINGLE_VALUE).text

        return color, chosen_color