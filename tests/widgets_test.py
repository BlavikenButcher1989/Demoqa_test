from pages.widgets_page import WidgetsPage
from pages.widgets_page import AutoCompletePage


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