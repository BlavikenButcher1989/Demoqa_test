import random

from selenium.webdriver.common.by import By


class FormPageLocators:
    # data
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    GENDER = (By.CSS_SELECTOR, f"label[for='gender-radio-{random.randint(1, 3)}']")
    MOBILE = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    DATE_OF_BIRTH = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')
    MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DAY = (By.CSS_SELECTOR, f"div[class*='react-datepicker__day react-datepicker__day--{('00' + str(random.randint(1, 28)))[-3]}']")
    SUBJECTS = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')
    HOBBIES = (By.CSS_SELECTOR, f'label[for="hobbies-checkbox-{random.randint(1, 3)}"]')
    FILE_INPUT = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')
    SELECT_STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    STATE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SELECT_CITY = (By.CSS_SELECTOR, 'div[id="city"]')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table result
    TABLE_RESULT = (By.XPATH, '//div[@class="table-responsive"]//td[2]')
