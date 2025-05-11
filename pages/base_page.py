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

    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView;", element)

    def click_on_element(self, element):
        self.driver.execute_script("arguments[0].click();", element)


    def delete_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")

    def delete_add(self):
        self.driver.execute_script("document.getElementById('fixedban')?.remove()")

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")

    def action_double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()
    def action_right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
