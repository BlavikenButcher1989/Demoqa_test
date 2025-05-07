import random
import time

from functions.functions import TextBoxPage
from functions.functions import CheckBoxPage
from functions.functions import RadioButtonPage
from functions.functions import WebTablePage
from functions.functions import ButtonsPage
from functions.functions import LinksPage
from functions.functions import UploadAndDownloadPage

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

    class TestButtonPage:

        def test_different_click_on_the_buttons(self, driver):
            button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            button_page.open_site()
            time.sleep(0.1)
            double = button_page.click_on_different_button('double')
            right = button_page.click_on_different_button('right')
            click = button_page.click_on_different_button('click')
            assert double == 'You have done a double click', "The double click button was not pressed"
            assert right == 'You have done a right click', "The right click button was not pressed"
            assert click == 'You have done a dynamic click', "The dynamic click button was not pressed"

    class TestLinksPage:

        def test_home_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open_site()
            href_link, current_url = links_page.check_home_link()
            try:
                assert href_link == current_url, 'The link is broken or url is incorrect'
            except:
                assert current_url == 400, f'Expected status code: 400, actual status code: {current_url}'

        def test_created_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open_site()
            response_code = links_page.check_created_link('https://demoqa.com/created')
            assert response_code == 201, 'Link works or status code is not 201'

        def test_no_content_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open_site()
            response_code = links_page.check_no_content_link('https://demoqa.com/no-content')
            assert response_code == 204, 'Link works or status code is not 204'

        def test_moved_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open_site()
            response_code = links_page.check_moved_link('https://demoqa.com/moved')
            assert response_code == 301, 'Link works or status code is not 301'

        def test_bad_request_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open_site()
            response_code = links_page.check_bad_request_link('https://demoqa.com/bad-request')
            assert response_code == 400, 'Link works or status code is not 400'

        def test_unauthorized_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open_site()
            response_code = links_page.check_unauthorized_link('https://demoqa.com/unauthorized')
            assert response_code == 401, 'Link works or status code is not 401'

        def test_forbidden_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open_site()
            response_code = links_page.check_forbidden_link('https://demoqa.com/forbidden')
            assert response_code == 403, 'Link works or status code is not 403'

        def test_not_found_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open_site()
            response_code = links_page.check_not_found_link('https://demoqa.com/invalid-url')
            assert response_code == 404, 'Link works or status code is not 404'

    class TestUploadAndDownload:

        def test_upload_file(self, driver):
            upload_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            upload_page.open_site()
            file_name, result_text = upload_page.upload_file()
            assert file_name == result_text, 'The file has not been uploaded'

        def test_download_file(self, driver):
            download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
            download_page.open_site()
            check = download_page.download_file()
            assert check is True, 'The file has not been downloaded'