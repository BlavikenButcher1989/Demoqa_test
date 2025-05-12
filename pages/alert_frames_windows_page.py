import random

from selenium.webdriver.support.wait import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from pages.base_page import BasePage

from generator.generator import generator_person
from locators.alert_frames_windows_locators import BrowserWindowsPageLocators
from locators.alert_frames_windows_locators import AlertsPageLocators
from locators.alert_frames_windows_locators import FramesPageLocators
from locators.alert_frames_windows_locators import NestedFramePageLocators
from locators.alert_frames_windows_locators import ModalDialogsPageLocators


class BrowserWindowPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

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

    def __init__(self, driver, url):
        super().__init__(driver, url)

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
        if random.randint(1, 2) == 1:
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


class FramesPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = FramesPageLocators()

    def check_frame(self, frame):
        if frame == 'frame_1':
            frame_1 = self.element_is_present(self.locators.FIRST_FRAME)
            width_1 = frame_1.get_attribute('width')
            height_1 = frame_1.get_attribute('height')
            self.switch_to_frame(frame_1)
            frame_title = self.element_is_present(self.locators.FRAME_TITLE).text
            self.driver.switch_to.default_content()

            return [width_1, height_1, frame_title]

        if frame == 'frame_2':
            frame_2 = self.element_is_present(self.locators.SECOND_FRAME)
            width_2 = frame_2.get_attribute('width')
            height_2 = frame_2.get_attribute('height')
            self.switch_to_frame(frame_2)
            frame_title = self.element_is_present(self.locators.FRAME_TITLE).text

            return [width_2, height_2, frame_title]


class NestedFramePage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = NestedFramePageLocators()

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.switch_to_frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.switch_to_frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_TEXT).text

        return parent_text, child_text


class ModalDialogsPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = ModalDialogsPageLocators()

    def check_small_modal(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        small_modal_text = self.element_is_visible(self.locators.SMALL_MODAL_TEXT).text
        small_title = self.element_is_visible(self.locators.SMALL_MODAL_TITLE).text
        self.element_is_visible(self.locators.SMALL_MODAL_CLOSE_BUTTON).click()

        return small_title, small_modal_text

    def check_large_modal(self):
        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        large_modal_text = self.element_is_visible(self.locators.LARGE_MODAL_TEXT).text
        large_title = self.element_is_visible(self.locators.LARGE_MODAL_TITLE).text
        self.element_is_visible(self.locators.LARGE_MODAL_CLOSE_BUTTON).click()

        return large_title, large_modal_text
