import time

from functions.functions import TextBoxPage


def test_open(driver):
    text_box_page = TextBoxPage(driver)
    text_box_page.open_site()
    full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
    output_name, output_email, output_cur_adr, output_per_addr = text_box_page.check_field_form()

    assert full_name == output_name
    assert email == output_email
    assert current_address == output_cur_adr
    assert permanent_address == output_per_addr