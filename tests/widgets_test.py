from data.data import menu_item_list

from pages.widgets_page import WidgetsPage
from pages.widgets_page import AutoCompletePage
from pages.widgets_page import DatePickerPage
from pages.widgets_page import SliderPage
from pages.widgets_page import ProgressBarPage
from pages.widgets_page import TabsPage
from pages.widgets_page import ToolTipsPage
from pages.widgets_page import MenuPage
from pages.widgets_page import SelectMenuPage


class TestWidgetsPage:

    class TestAccordianPage:

        def test_accordian(self, driver):
            accordian_page = WidgetsPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open_site()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and len(first_content) > 0, 'Widget does not exist or empty content'
            assert second_title == 'Where does it come from?' and len(second_content) > 0, 'Widget does not exist or empty content'
            assert third_title == 'Why do we use it?' and len(third_content) > 0, 'Widget does not exist or empty content'

    class TestAutoCompletePage:

        def test_fill_and_remove_multi_complete(self, driver):
            auto_complete = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete.open_site()
            colors, chosen_colors, count_colors_before, count_colors_after = auto_complete.check_fill_input_multi()
            assert colors == chosen_colors, 'Adding colors was missed in the input'
            assert count_colors_before != count_colors_after, 'Color did not delete'

        def test_fill_input_complete(self, driver):
            auto_complete = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            auto_complete.open_site()
            color, chosen_color = auto_complete.check_fill_input_single()
            assert color == chosen_color, 'Color was not added'

    class TestDatePickerPage:

        def test_date_input(self, driver):
            date_input = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_input.open_site()
            value_date_before, value_date_after = date_input.check_select_date()
            assert value_date_before != value_date_after, 'Data has not been changed'

        def test_date_and_time_input(self, driver):
            date_and_time_input = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_and_time_input.open_site()
            value_date_before, value_date_after = date_and_time_input.check_select_date_and_time()
            assert value_date_before != value_date_after, 'Data and time has not been changed'


    class TestSliderPage:

        def test_slider(self, driver):
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open_site()
            value_before, value_after = slider_page.check_change_slider_value()
            assert value_before != value_after

    class TestProgressBarPage:

        def test_progress_bar(self, driver):
            progress_bar = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar.open_site()
            value_before, value_after = progress_bar.check_change_progress_bar_value()
            assert value_before != value_after, 'Progress bar value has not been changed'


    class TestTabsPage:

        def test_tabs(self, driver):
            tabs = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs.open_site()
            tab_what_title, tab_what_content = tabs.check_tabs('what')
            tab_origin_title, tab_origin_content = tabs.check_tabs('origin')
            tab_use_title, tab_use_content = tabs.check_tabs('use')
            assert tab_what_title == 'What' and tab_what_content > 0, 'Tab "What" was not pressed or text was missed'
            assert tab_origin_title == 'Origin' and tab_origin_content > 0, 'Tab "Origin" was not pressed or text was missed'
            assert tab_use_title == 'Use' and tab_use_content > 0, 'Tab "Use" was not pressed or text was missed'


    class TestToolTipsPage:

        def test_tool_tips(self, driver):
            toll_tips = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            toll_tips.open_site()
            text_button, text_field, text_contrary, text_section = toll_tips.check_tool_tips()
            assert text_button == 'You hovered over the Button'
            assert text_field == 'You hovered over the text field'
            assert text_contrary == 'You hovered over the Contrary'
            assert text_section == 'You hovered over the 1.10.32'


    class TestMenuPage:

        def test_menu(self, driver):
            menu_page = MenuPage(driver, 'https://demoqa.com/menu#')
            menu_page.open_site()
            data = menu_page.check_menu()
            assert data == menu_item_list, 'Menu items do not exist or have not been selected'

    class TestSelectMenuPage:

        def test_select_option(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open_site()
            select_option_text_before, select_option_text_after = select_menu_page.check_select_option()
            assert select_option_text_before != select_option_text_after, 'Option have not been chosen'

        def test_select_title(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open_site()
            select_title_text_before, select_title_text_after = select_menu_page.check_select_title()
            assert select_title_text_before != select_title_text_after, 'Title have not been chosen'

        def test_old_select(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open_site()
            colors, text = select_menu_page.check_old_select()
            assert text in colors, 'Color have not been chosen'

        def test_multiselect(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open_site()
            colors, multiselect_colors = select_menu_page.check_multiselect()
            assert colors == multiselect_colors, 'Colors have not been chosen'

        def test_standard_select(self, driver):
            select_menu_page = SelectMenuPage(driver, 'https://demoqa.com/select-menu')
            select_menu_page.open_site()
            cars, text = select_menu_page.check_standard_select()
            assert text in cars, 'Car have not been chosen'