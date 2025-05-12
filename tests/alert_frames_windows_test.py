from pages.alert_frames_windows_page import BrowserWindowPage
from pages.alert_frames_windows_page import AlertsPage
from pages.alert_frames_windows_page import FramesPage
from pages.alert_frames_windows_page import NestedFramePage
from pages.alert_frames_windows_page import ModalDialogsPage

class TestAlertsFramesWindows:

    class TestBrowserWindowsPage:

        def test_new_tab(self, driver):
            new_tab_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            new_tab_page.open_site()
            new_tab_text = new_tab_page.check_new_tab()
            assert 'This is a sample page' == new_tab_text, 'New tab has not opened or an incorrect tab has opened'

        def test_new_window(self, driver):
            new_window_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            new_window_page.open_site()
            new_window_text = new_window_page.check_new_window()
            assert 'This is a sample page' == new_window_text, 'New window has not opened or an incorrect window has opened'

    class TestAlertsPage:

        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open_site()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button', 'Alert did not appear'

        def test_see_alert_after_5_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open_site()
            alert_text = alert_page.check_see_alert_after_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', 'Alert did not appear'

        def test_confirm_box_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open_site()
            alert_text, result_text = alert_page.check_confirm_box_alert()
            assert alert_text == 'Do you confirm action?', 'Alert did not appear'
            assert result_text == 'You selected Ok' or 'You selected Cancel', 'Alert buttons do not work'

        def test_prompt_box_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open_site()
            name, alert_text, input_result = alert_page.check_prompt_box_alert()
            assert alert_text == 'Please enter your name', 'Alert did not appear'
            assert input_result == name, 'Field was not filled'

    class TestFramePage:

        def test_frame(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open_site()
            result_frame_1 = frame_page.check_frame('frame_1')
            result_frame_2 = frame_page.check_frame('frame_2')
            assert result_frame_1 == ['500px', '350px', 'This is a sample page'], 'Frame does not exist'
            assert result_frame_2 == ['100px', '100px', 'This is a sample page'], 'Frame does not exist'

    class TestNestedFramePage:

        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramePage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open_site()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == 'Parent frame', 'Nested frame does not exist'
            assert child_text == 'Child Iframe', 'Nested frame does not exist'

    class TestModalDialogsPage:

        def test_small_modal(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open_site()
            small_title, small_modal_text = modal_dialogs_page.check_small_modal()
            assert small_title == 'Small Modal', 'Title is not Small Modal'
            assert small_modal_text == 'This is a small modal. It has very less content', 'Dialog text does not match'

        def test_large_modal(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open_site()
            large_title, large_modal_text = modal_dialogs_page.check_large_modal()
            assert large_title == 'Large Modal', 'Title is not Large Modal'
            assert 'Lorem Ipsum is simply dummy text' in large_modal_text, 'Dialog text does not match'
