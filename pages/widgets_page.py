from selenium.common import TimeoutException

from locators.widgets_locators import WidgetsPageLocators
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