from pages.widgets_page import WidgetsPage


class TestWidgetsPage:

    class TestAccordian:

        def test_accordian(self, driver):
            accordian_page = WidgetsPage(driver, 'https://demoqa.com/accordian')
            accordian_page.open_site()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')
            assert first_title == 'What is Lorem Ipsum?' and len(first_content) > 0, 'Widget does not exist or empty content'
            assert second_title == 'Where does it come from?' and len(second_content) > 0, 'Widget does not exist or empty content'
            assert third_title == 'Why do we use it?' and len(third_content) > 0, 'Widget does not exist or empty content'