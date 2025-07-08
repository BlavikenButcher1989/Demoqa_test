from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as W
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_site(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator):
        return W(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator):
        return W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator):
        return W(self.driver, 10).until(EC.presence_of_element_located(locator))

    def elements_are_present(self, locator):
        return W(self.driver, 10).until(EC.presence_of_all_elements_located(locator))

    def element_is_not_visible(self, locator):
        return W(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator):
        return W(self.driver, 10).until(EC.element_to_be_clickable(locator))


    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def switch_to_frame(self, locator):
        self.driver.switch_to.frame(locator)