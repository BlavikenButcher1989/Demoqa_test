import random
import time

from functions.functions import TextBoxPage
from functions.functions import CheckBoxPage
from functions.functions import RadioButtonPage
from functions.functions import WebTablePage

class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open_site()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_adr, output_per_addr = text_box_page.check_field_form()

            assert full_name == output_name, "the full name doesn't match"
            assert email == output_email, "the email doesn't match"
            assert current_address == output_cur_adr, "the current address doesn't match"
            assert permanent_address == output_per_addr, "the permanent address doesn't match"

    class TestCheckBox:

        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open_site()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_result = check_box_page.get_output_result()
            print(input_checkbox)
            print(output_result)
            assert input_checkbox == output_result, "checkboxes have not been selected"


    class TestRadioButton:

        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open_site()
            radio_button_page.click_on_the_radio_button('yes')
            output_yes = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('impressive')
            output_impressive = radio_button_page.get_output_result()
            radio_button_page.click_on_the_radio_button('no')
            time.sleep(3)
            output_no = radio_button_page.get_output_result()
            assert output_yes == 'Yes', "'Yes' have not been selected"
            assert output_impressive == 'Impressive', "'Impressive' have not been selected"
            assert output_no == 'No', "'No' have not been selected"


    class TestWebTable:

        def test_web_table_and_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open_site()
            input_data = web_table_page.add_new_person()
            output_data = web_table_page.check_new_added_person()
            assert input_data in output_data

        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open_site()
            key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_some_person(key_word)
            table_result = web_table_page.check_search_person()
            assert key_word in table_result, "the person was not found in the table"

        def test_web_table_update_person_info(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open_site()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_some_person(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_search_person()
            assert age in row, "the person card has changed"

        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open_site()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_some_person(email)
            web_table_page.delete_persone()
            text = web_table_page.check_deleted()
            assert text == "No rows found"

        def test_web_table_change_count_row(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open_site()
            expected_rows_count = [5, 10, 20, 25, 50, 100]
            actual_rows_count = web_table_page.select_up_to_some_rows()
            assert actual_rows_count == expected_rows_count, (
        f"Количество строк не соответствует ожидаемому. "
        f"Ожидалось: {expected_rows_count}, Фактически: {actual_rows_count}"
    )