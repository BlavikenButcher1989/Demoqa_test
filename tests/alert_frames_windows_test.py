from pages.alert_frames_windows_page import BrowserWindowPage
from pages.alert_frames_windows_page import AlertsPage

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
