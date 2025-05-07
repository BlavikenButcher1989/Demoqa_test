from selenium.webdriver.common.by import By

class TextBoxPageLocators:

    FULL_NAME = (By.XPATH, "//input[@id='userName']")
    EMAIL = (By.XPATH, "//input[@id='userEmail']")
    CURRENT_ADDRESS = (By.XPATH, "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = (By.XPATH, "//textarea[@id='permanentAddress']")
    SUBMIT = (By.XPATH, "//button[@id='submit']")

    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')

class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class="text-success"]')

class RadioButtonLocators:

    YES_RADIO_BUTTON = (By.CSS_SELECTOR, 'label[for="yesRadio"]')
    IMPRESSIVE_RADIO_BUTTON = (By.CSS_SELECTOR, 'label[for="impressiveRadio"]')
    NO_RADIO_BUTTON = (By.CSS_SELECTOR, 'label[for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")

class WebTablePageLocators:

    # add person form
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_BUTTON = (By.XPATH, './/ancestor::div[@class="rt-tr-group"]')
    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')
    COUNT_ROW_LIST = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')

class ButtonsPageLocators:

    #buttons
    DOUBLE_BUTTON = (By.XPATH, '//div[1]/button')
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    CLICK_ME_BUTTON = (By.XPATH, "//div[3]/button")

    #result
    SUCCESS_DOUBLE = (By.CSS_SELECTOR, '#doubleClickMessage')
    SUCCESS_RIGHT = (By.CSS_SELECTOR, '#rightClickMessage')
    SUCCESS_CLICK_ME = (By.CSS_SELECTOR, '#dynamicClickMessage')