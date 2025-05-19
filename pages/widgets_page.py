import random
import time

from data.data import color_list

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.select import Select

from locators.widgets_locators import WidgetsPageLocators
from locators.widgets_locators import AutoCompletePageLocators
from locators.widgets_locators import DatePickerPageLocators
from locators.widgets_locators import SliderPageLocators
from locators.widgets_locators import ProgressBarPageLocators
from locators.widgets_locators import TabsPageLocators

from pages.base_page import BasePage

from generator.generator import generator_date


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

class DatePickerPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = DatePickerPageLocators()

    def check_select_date(self):
        date = next(generator_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')

        return value_date_before, value_date_after

    def check_select_date_and_time(self):
        date = next(generator_date())
        input_date_and_time = self.element_is_visible(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date_and_time.get_attribute('value')
        input_date_and_time.click()
        self.element_is_clickable(self.locators.DATE_AND_TIME_SELECT_MONTH).click()
        self.set_date_from_list(self.locators.DATE_AND_TIME_MONTHS_LIST, date.month)
        self.element_is_clickable(self.locators.DATE_AND_TIME_SELECT_YEAR).click()
        self.set_date_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, '2020')
        self.set_date_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        time_list = self.elements_are_present(self.locators.DATE_AND_TIME_TIME_LIST)
        time_ = random.choice(time_list)
        time_.click()
        value_date_after = input_date_and_time.get_attribute('value')

        return value_date_before, value_date_after

    def set_date_by_text(self, element, value):
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_from_list(self, elements, value):
        item_list = self.elements_are_visible(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break

class SliderPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = SliderPageLocators()

    def check_change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.INPUT_SLIDER)
        time.sleep(0.1)
        self.slide_drag_and_drop(slider_input, random.randint(1, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')

        return value_before, value_after

class ProgressBarPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = ProgressBarPageLocators()

    def check_change_progress_bar_value(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_visible(self.locators.PROGRESS_BAR_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(2, 5))
        progress_bar_button.click()
        value_after = self.element_is_visible(self.locators.PROGRESS_BAR_VALUE).text

        return value_before, value_after

class TabsPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = TabsPageLocators()

    def check_tabs(self, name):

        names = {
            'what': {
                'title': self.locators.TAB_WHAT,
                'text': self.locators.TAB_WHAT_TEXT
            },
            'origin': {
                'title': self.locators.TAB_ORIGIN,
                'text': self.locators.TAB_ORIGIN_TEXT
            },
            'use': {
                'title': self.locators.TAB_USE,
                'text': self.locators.TAB_USE_TEXT
            }
        }

        tab_title = self.element_is_visible(names[name]['title'])
        tab_title.click()
        tab_text = self.element_is_visible(names[name]['text']).text



        return tab_title.text, len(tab_text)