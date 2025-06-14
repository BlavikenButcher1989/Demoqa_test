from pages.interations_page import SortablePage
from pages.interations_page import SelectablePage


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

class TestSelectablePage:

    def test_selectable_list(self, driver):
        selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
        selectable_page.open_site()
        count_item, item_list_active = selectable_page.change_list_order()
        assert count_item == item_list_active, 'elements were not selected'

    def test_selectable_grid(self, driver):
        selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
        selectable_page.open_site()
        count_item, item_grid_active = selectable_page.change_grid_order()
        assert count_item == item_grid_active, 'elements were not selected'