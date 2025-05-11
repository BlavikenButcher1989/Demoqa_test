from pages.alert_frames_windows_page import BrowserWindowPage

class TestAlertsFramesWindows:

    class TestBrowserWindows:

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