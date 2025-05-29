from selenium.webdriver.common.by import By


class WidgetsPageLocators:

    SECTION_FIRST = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    SECTION_CONTENT_FIRST = (By.CSS_SELECTOR, 'div[id="section1Content"] p')

    SECTION_SECOND = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECTION_CONTENT_SECOND = (By.CSS_SELECTOR, 'div[id="section2Content"] p')

    SECTION_THIRD = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    SECTION_CONTENT_THIRD = (By.CSS_SELECTOR, 'div[id="section3Content"] p')

class AutoCompletePageLocators:

    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')

    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')

class DatePickerPageLocators:

    DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_AND_TIME_SELECT_MONTH = (By.CSS_SELECTOR, 'span[class="react-datepicker__month-read-view--down-arrow"]')
    DATE_AND_TIME_MONTHS_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__month-option"]')
    DATE_AND_TIME_SELECT_YEAR = (By.CSS_SELECTOR, 'span[class="react-datepicker__year-read-view--down-arrow"]')
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__year-option"]')
    DATE_AND_TIME_TIME_LIST = (By.CSS_SELECTOR, 'li[class^="react-datepicker__time-list-item "]')

class SliderPageLocators:

    INPUT_SLIDER = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')

class ProgressBarPageLocators:

    PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')

class TabsPageLocators:

    TAB_WHAT = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')
    TAB_WHAT_TEXT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"] p')

    TAB_ORIGIN = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')
    TAB_ORIGIN_TEXT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"] p')

    TAB_USE = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')
    TAB_USE_TEXT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"] p')

class ToolTipsPageLocators:

    BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')
    TOOL_TIP_BUTTON = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')

    FIELD = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')
    TOOL_TIP_FIELD = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

    LINK_CONTRARY = (By.XPATH, "//a[contains(text(), 'Contrary')]")
    TOOL_TIP_CONTRARY = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')

    LINK_SECTION = (By.XPATH, "//a[contains(text(), '1.10.32')]")
    TOOL_TIP_SECTION = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    TOOL_TIPS_INNERS = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')

class MenuPageLocators:

    MAIN_ITEM_LIST = (By.CSS_SELECTOR, 'ul[id="nav"] li a')

class SelectMenuPageLocators:

    SELECT_OPTION = (By.CSS_SELECTOR, 'input[id="react-select-2-input"]')
    SELECT_OPTION_TEXT_BEFORE_SELECT = (By.CSS_SELECTOR, 'div[class=" css-1wa3eu0-placeholder"]')
    SELECT_OPTION_TEXT_AFTER_SELECT = (By.CSS_SELECTOR, 'div[class=" css-1uccc91-singleValue"]')

    SELECT_TITLE = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SELECT_TITLE_TEXT_BEFORE_SELECT = (By.CSS_SELECTOR, 'div[class=" css-1wa3eu0-placeholder"]')
    SELECT_TITLE_TEXT_AFTER_SELECT = (By.CSS_SELECTOR, 'div[class=" css-1uccc91-singleValue"]')

    OLD_SELECT = (By.CSS_SELECTOR, 'select[id="oldSelectMenu"]')

    MULTISELECT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')
    MULTISELECT_TEXT = (By.CSS_SELECTOR, 'div[class="css-12jo7m5"]')

    STANDARD_SELECT = (By.CSS_SELECTOR, 'select[id="cars"]')