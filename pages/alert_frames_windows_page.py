import time

from pages.base_page import BasePage
from locators.alert_frames_windows_locators import BrowserWindowsPageLocators

class BrowserWindowPage(BasePage):

    locators = BrowserWindowsPageLocators()

    def check_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.switch_to_new_tab()
        result_text = self.element_is_present(self.locators.NEW_TAB_TEXT).text

        return result_text

    def check_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.switch_to_new_tab()
        result_text = self.element_is_present(self.locators.NEW_TAB_TEXT).text
        print(result_text)

        return result_text
