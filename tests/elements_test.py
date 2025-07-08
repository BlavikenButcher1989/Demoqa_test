import random
import time
import allure

from pages.elements_page import TextBoxPage
from pages.elements_page import CheckBoxPage
from pages.elements_page import RadioButtonPage
from pages.elements_page import WebTablePage
from pages.elements_page import ButtonsPage
from pages.elements_page import LinksPage
from pages.elements_page import UploadAndDownloadPage
from pages.elements_page import DynamicPropertiesPage


@allure.suite('Elements')
class TestElements:
    @allure.description('TextBox')
    class TestTextBox:
        @allure.title('Check TextBox')
        def test_text_box(self, driver):
            with allure.step('Open TextBox Page'):
                text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
                text_box_page.open_site()
            with allure.step('Fill all fields'):
                full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            with allure.step('Get output values'):
                output_name, output_email, output_cur_adr, output_per_addr = text_box_page.check_field_form()
            with allure.step('Verify full name'):
                assert full_name == output_name, "the full name doesn't match"
            with allure.step('Verify email'):
                assert email == output_email, "the email doesn't match"
            with allure.step('Verify current address'):
                assert current_address == output_cur_adr, "the current address doesn't match"
            with allure.step('Verify permanent address'):
                assert permanent_address == output_per_addr, "the permanent address doesn't match"

    @allure.description('CheckBox')
    class TestCheckBox:
        @allure.title('Check CheckBox')
        def test_check_box(self, driver):
            with allure.step('Open CheckBox Page'):
                check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
                check_box_page.open_site()
            with allure.step('Expend all checkboxes'):
                check_box_page.open_full_list()
            with allure.step('Click on random checkboxes'):
                check_box_page.click_random_checkbox()
            with allure.step('Get selected checkboxes'):
                input_checkbox = check_box_page.get_checked_checkboxes()
            with allure.step('Get result list of selected checkboxes'):
                output_result = check_box_page.get_output_result()
            with allure.step('Check that selected checkboxes compare with checkboxes in result list'):
                assert input_checkbox == output_result, "checkboxes have not been selected"

    @allure.description('RadioButton')
    class TestRadioButton:
        @allure.title('Check RadioButton')
        def test_radio_button(self, driver):
            with allure.step('Open RadioButton Page'):
                radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
                radio_button_page.open_site()
            with allure.step('Click on the button "Yes"'):
                radio_button_page.click_on_the_radio_button('yes')
            with allure.step('Get clicked result "Yes"'):
                output_yes = radio_button_page.get_output_result()
            with allure.step('Click on the button "Impressive"'):
                radio_button_page.click_on_the_radio_button('impressive')
            with allure.step('Get clicked result "Impressive"'):
                output_impressive = radio_button_page.get_output_result()
            with allure.step('Check that radio button "Yes" is selected'):
                assert output_yes == 'Yes', "'Yes' have not been selected"
            with allure.step('Check that radio button "Yes" is selected'):
                assert output_impressive == 'Impressive', "'Impressive' have not been selected"

    @allure.description('WebTable')
    class TestWebTable:
        @allure.title('Check add person to the table')
        def test_web_table_and_person(self, driver):
            with allure.step('Open WebTable Page'):
                web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
                web_table_page.open_site()
            with allure.step('Add new person'):
                input_data = web_table_page.add_new_person()
            with allure.step('Get added person info'):
                output_data = web_table_page.check_new_added_person()
            with allure.step('Check that new person exist in persons list'):
                assert input_data in output_data

        @allure.title('Check search person')
        def test_web_table_search_person(self, driver):
            with allure.step('Open WebTable Page'):
                web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
                web_table_page.open_site()
            with allure.step('Add new person and choose random data of this person'):
                key_word = web_table_page.add_new_person()[random.randint(0, 5)]
            with allure.step('Search person by the chosen data'):
                web_table_page.search_some_person(key_word)
            with allure.step('Get result of searching person'):
                table_result = web_table_page.check_search_person()
            with allure.step('Get count of persons after search'):
                count_of_persons = web_table_page.check_new_added_person()
            with allure.step('Check that data of new person is in person info'):
                assert key_word in table_result, "the person was not found in the table"
            with allure.step('Check that count of searching persons is 1'):
                assert len(list(count_of_persons)) == 1

        @allure.title('Check update person info')
        def test_web_table_update_person_info(self, driver):
            with allure.step('Open WebTable Page'):
                web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
                web_table_page.open_site()
            with allure.step('Add new person and get lastname'):
                lastname = web_table_page.add_new_person()[1]
            with allure.step('Search person by the lastname'):
                web_table_page.search_some_person(lastname)
            with allure.step('Change age of person'):
                age = web_table_page.update_person_info()
            with allure.step('Get update person info'):
                row = web_table_page.check_search_person()
            with allure.step('Check that age is changed'):
                assert age in row, "the person card has changed"

        @allure.title('Check delete person')
        def test_web_table_delete_person(self, driver):
            with allure.step('Open WebTable Page'):
                web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
                web_table_page.open_site()
            with allure.step('Add new person and get email'):
                email = web_table_page.add_new_person()[3]
            with allure.step('Search person by the email'):
                web_table_page.search_some_person(email)
            with allure.step('Delete person'):
                web_table_page.delete_person()
            with allure.step('Get conformation text after delete'):
                text = web_table_page.check_deleted()
            with allure.step('Check that person is deleted'):
                assert text == "No rows found"

        @allure.title('Check change count row')
        def test_web_table_change_count_row(self, driver):
            with allure.step('Open WebTable Page'):
                web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
                web_table_page.open_site()
            expected_rows_count = [5, 10, 20, 25, 50, 100]
            with allure.step('Select rows'):
                actual_rows_count = web_table_page.select_up_to_some_rows()
            with allure.step('Check that actual rows count compare with expected rows count'):
                assert actual_rows_count == expected_rows_count, (
        f"The number of lines does not match the expected number. "
        f"Expected: {expected_rows_count}, Actually: {actual_rows_count}"
    )

    @allure.description('ButtonPage')
    class TestButtonPage:

        @allure.title('Check different click on the buttons')
        def test_different_click_on_the_buttons(self, driver):
            with allure.step('Open Button Page'):
                button_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
                button_page.open_site()
            time.sleep(0.1)
            with allure.step('Double click on the button'):
                double = button_page.click_on_different_button('double')
            with allure.step('Right click on the button'):
                right = button_page.click_on_different_button('right')
            with allure.step('Dynamic click on the button'):
                click = button_page.click_on_different_button('click')
            with allure.step('Check that double click is worked and clicking text result is displayed'):
                assert double == 'You have done a double click', "The double click button was not pressed"
            with allure.step('Check that right click is worked and clicking text result is displayed'):
                assert right == 'You have done a right click', "The right click button was not pressed"
            with allure.step('Check that dynamic click is worked and clicking text result is displayed'):
                assert click == 'You have done a dynamic click', "The dynamic click button was not pressed"

    @allure.description('LinksPage')
    class TestLinksPage:

        @allure.title('Check Home Link')
        def test_home_link(self, driver):
            with allure.step('Open Links Page'):
                links_page = LinksPage(driver, 'https://demoqa.com/links')
                links_page.open_site()
            with allure.step('Open Home link, get home link url and current url'):
                href_link, current_url = links_page.check_home_link()
            with allure.step('Check that Home link url compare with current url'):
                try:
                    assert href_link == current_url, 'The link is broken or url is incorrect'
                except:
                    assert current_url == 400, f'Expected status code: 400, actual status code: {current_url}'

        @allure.title('Check Created Link')
        def test_created_link(self, driver):
            with allure.step('Open Links Page'):
                links_page = LinksPage(driver, 'https://demoqa.com/links')
                links_page.open_site()
            with allure.step('Open Created link and get status code'):
                response_code = links_page.check_created_link('https://demoqa.com/created')
            with allure.step('Check that status code is 201'):
                assert response_code == 201, 'Link works or status code is not 201'
        @allure.title('Check No Content Link')
        def test_no_content_link(self, driver):
            with allure.step('Open Links Page'):
                links_page = LinksPage(driver, 'https://demoqa.com/links')
                links_page.open_site()
            with allure.step('Open No Content link and get status code'):
                response_code = links_page.check_no_content_link('https://demoqa.com/no-content')
            with allure.step('Check that status code is 204'):
                assert response_code == 204, 'Link works or status code is not 204'
        @allure.title('Check Moved Link')
        def test_moved_link(self, driver):
            with allure.step('Open Links Page'):
                links_page = LinksPage(driver, 'https://demoqa.com/links')
                links_page.open_site()
            with allure.step('Open Moved link and get status code'):
                response_code = links_page.check_moved_link('https://demoqa.com/moved')
            with allure.step('Check that status code is 301'):
                assert response_code == 301, 'Link works or status code is not 301'
        @allure.title('Check Bad Request Link')
        def test_bad_request_link(self, driver):
            with allure.step('Open Links Page'):
                links_page = LinksPage(driver, 'https://demoqa.com/links')
                links_page.open_site()
            with allure.step('Open Bad Request link and get status code'):
                response_code = links_page.check_bad_request_link('https://demoqa.com/bad-request')
            with allure.step('Check that status code is 400'):
                assert response_code == 400, 'Link works or status code is not 400'
        @allure.title('Check Unauthorized Link')
        def test_unauthorized_link(self, driver):
            with allure.step('Open Links Page'):
                links_page = LinksPage(driver, 'https://demoqa.com/links')
                links_page.open_site()
            with allure.step('Open Unauthorized link and get status code'):
                response_code = links_page.check_unauthorized_link('https://demoqa.com/unauthorized')
            with allure.step('Check that status code is 401'):
                assert response_code == 401, 'Link works or status code is not 401'
        @allure.title('Check Forbidden Link')
        def test_forbidden_link(self, driver):
            with allure.step('Open Links Page'):
                links_page = LinksPage(driver, 'https://demoqa.com/links')
                links_page.open_site()
            with allure.step('Open Forbidden link and get status code'):
                response_code = links_page.check_forbidden_link('https://demoqa.com/forbidden')
            with allure.step('Check that status code is 403'):
                assert response_code == 403, 'Link works or status code is not 403'
        @allure.title('Check Not Found Link')
        def test_not_found_link(self, driver):
            with allure.step('Open Links Page'):
                links_page = LinksPage(driver, 'https://demoqa.com/links')
                links_page.open_site()
            with allure.step('Open Not Found link and get status code'):
                response_code = links_page.check_not_found_link('https://demoqa.com/invalid-url')
            with allure.step('Check that status code is 404'):
                assert response_code == 404, 'Link works or status code is not 404'

    @allure.description('UploadAndDownload')
    class TestUploadAndDownload:
        @allure.title('Check Upload File')
        def test_upload_file(self, driver):
            with allure.step('Open UploadAndDownload Page'):
                upload_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
                upload_page.open_site()
            with allure.step('Upload file, get file name and uploading result text'):
                file_name, result_text = upload_page.upload_file()
            with allure.step('Check that file name compare with result text'):
                assert file_name == result_text, 'The file has not been uploaded'
        @allure.title('Check Download File')
        def test_download_file(self, driver):
            with allure.step('Open UploadAndDownload Page'):
                download_page = UploadAndDownloadPage(driver, 'https://demoqa.com/upload-download')
                download_page.open_site()
            with allure.step('Download file'):
                check = download_page.download_file()
            with allure.step('Check that download file is exist'):
                assert check is True, 'The file has not been downloaded'

    @allure.description('DynamicPropertiesPage')
    class TestDynamicPropertiesPage:
        @allure.title('Check Enable Button')
        def test_check_enable_button(self, driver):
            with allure.step('Open DynamicProperties Page'):
                dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
                dynamic_properties_page.open_site()
            with allure.step('Wait 5 seconds'):
                enable_button = dynamic_properties_page.check_enable_button()
            with allure.step('Check that button is enabled after 5 seconds'):
                assert enable_button is True, 'The button has not enabled after 5 seconds'
        @allure.title('Check Change Color Button')
        def test_change_color_button(self, driver):
            with allure.step('Open DynamicProperties Page'):
                dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
                dynamic_properties_page.open_site()
            with allure.step('Get button final colors'):
                final_color_button = 'rgba(220, 53, 69, 1)'
            with allure.step('Get button colors after click'):
                color_button_after = dynamic_properties_page.check_changed_color()
            with allure.step('Check that button final colors compare with button colors after click'):
                assert final_color_button == color_button_after, "Final color of the button did not match with it's actual color"
        @allure.title('Check Appear Button')
        def test_appear_button(self, driver):
            with allure.step('Open DynamicProperties Page'):
                dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
                dynamic_properties_page.open_site()
            with allure.step('Wait for appearing button and get time'):
                appear_button, wait_time = dynamic_properties_page.check_appear_of_button()
            with allure.step('Check that the button is appeared'):
                assert appear_button is True, f'The button has not appeared after 5 seconds'
            with allure.step('Check that time of waiting is 5 seconds'):
                assert wait_time == 5, 'Time more or less than 5 seconds '