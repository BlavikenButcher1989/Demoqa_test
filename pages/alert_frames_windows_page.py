import random


from selenium.webdriver.support.wait import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from pages.base_page import BasePage

from generator.generator import generator_person
from locators.alert_frames_windows_locators import BrowserWindowsPageLocators
from locators.alert_frames_windows_locators import AlertsPageLocators

class BrowserWindowPage(BasePage):

    locators = BrowserWindowsPageLocators()

    def check_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.switch_to_new_tab()
        result_text = self.element_is_present(self.locators.RESULT_TEXT).text

        return result_text

    def check_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.switch_to_new_tab()
        result_text = self.element_is_present(self.locators.RESULT_TEXT).text
        print(result_text)

        return result_text

class AlertsPage(BasePage):

    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_text = Alert(self.driver).text
        Alert(self.driver).accept()

        return alert_text

    def check_see_alert_after_5_sec(self):
        self.element_is_visible(self.locators.SEE_ALERT_AFTER_5_SEC_BUTTON).click()
        W(self.driver, 10).until(EC.alert_is_present())
        alert_text = Alert(self.driver).text
        Alert(self.driver).accept()

        return alert_text

    def check_confirm_box_alert(self):
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert = Alert(self.driver)
        alert_text = alert.text
        if random.randint(1 ,2) == 1:
            alert.accept()
        else:
            alert.dismiss()
        result_text = self.element_is_present(self.locators.CONFIRM_BOX_RESULT).text

        return alert_text, result_text


    def check_prompt_box_alert(self):
        person = next(generator_person())
        name = person.firstname
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert = Alert(self.driver)
        alert_text = alert.text
        alert.send_keys(name)
        alert.accept()
        input_result = self.element_is_present(self.locators.PROMPT_BOX_RESULT).text

        return name, alert_text, input_result.split()[2]