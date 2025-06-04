from pages.interations_page import SortablePage


class TestSortablePage:

    def test_sortable_list(self, driver):
        sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
        sortable_page.open_site()
        order_before, order_after = sortable_page.change_list_order()
        assert order_before != order_after, 'Order of teh list has not been changed'

    def test_sortable_grid(self, driver):
        sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
        sortable_page.open_site()
        order_before, order_after = sortable_page.change_grid_order()
        assert order_before != order_after, 'Order of teh grid has not been changed'