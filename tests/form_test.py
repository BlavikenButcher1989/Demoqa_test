from pages.form_page import FormPage

class TestForm:

    class TestFormPage:

        def test_form(self, driver):
            form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            form_page.open_site()
            p, gender, year, subject, hobbies, file_name, state, city = form_page.fill_form_fields()
            result_list = form_page.check_result()
            assert p.firstname + ' ' + p.lastname == result_list[0], 'Firstname or lastname did not match'
            assert p.email == result_list[1], 'Email did not match'
            assert gender == result_list[2], 'Gender did not match'
            assert p.mobile == result_list[3], 'Mobile did not match'
            assert year in result_list[4], 'Year did not match'
            assert subject == result_list[5], 'Subject did not match'
            assert hobbies == result_list[6], 'Hobbies did not match'
            assert file_name == result_list[7], 'Filename did not match'
            assert p.current_address == result_list[8], 'Address did not match'
            assert state + ' ' + city == result_list[9], 'State or city did not match'
