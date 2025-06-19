from pages.interations_page import SortablePage
from pages.interations_page import SelectablePage
from pages.interations_page import ResizablePage
from pages.interations_page import DroppablePage


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

class TestResizablePage:

    def test_resizable_box(self, driver):
        resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
        resizable_page.open_site()
        max_size, min_size = resizable_page.change_size_resizable_box()
        assert max_size == '500, 300'
        assert min_size == '150, 150'

    def test_resizable(self, driver):
        resizable_page = ResizablePage(driver, 'https://demoqa.com/resizable')
        resizable_page.open_site()
        max_size, min_size = resizable_page.change_size_resizable()
        assert max_size != min_size

class TestDroppablePage:

    def test_simple(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open_site()
        text_before_drop, text_after_drop = droppable_page.check_simple()
        assert text_before_drop == 'Drop here'
        assert text_after_drop == 'Dropped!', 'Element has not been dropped'

    def test_acceptable(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open_site()
        text_before_drop, text_after_drop = droppable_page.check_acceptable()
        assert text_before_drop == 'Drop here'
        assert text_after_drop == 'Dropped!', 'Element has not been accepted'

    def test_not_acceptable(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open_site()
        text_before_drop, text_after_drop = droppable_page.check_not_acceptable()
        assert text_before_drop == 'Drop here'
        assert text_after_drop == 'Drop here', 'Element has been accepted'

    def test_prevent_propogation_not_greedy(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open_site()
        (text_outer_droppable_before_drop, text_inner_droppable_before_drop,
         text_outer_droppable_after_drop, text_inner_droppable_after_drop) = droppable_page.check_prevent_propogation('not greedy')
        assert text_outer_droppable_before_drop == 'Outer droppable'
        assert text_inner_droppable_before_drop == 'Inner droppable (not greedy)'
        assert text_outer_droppable_after_drop == 'Dropped!', 'Element has not been dropped'
        assert text_inner_droppable_after_drop == 'Dropped!', 'Element has not been dropped'

    def test_prevent_propogation_greedy_inner(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open_site()
        (text_outer_droppable_before_drop, text_inner_droppable_before_drop,
         text_outer_droppable_after_drop, text_inner_droppable_after_drop) = droppable_page.check_prevent_propogation('greedy inner')
        assert text_outer_droppable_before_drop == 'Outer droppable'
        assert text_inner_droppable_before_drop == 'Inner droppable (greedy)'
        assert text_outer_droppable_after_drop == 'Outer droppable'
        assert text_inner_droppable_after_drop == 'Dropped!', 'Element has not been dropped'

    def test_prevent_propogation_greedy_outer(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open_site()
        (text_outer_droppable_before_drop, text_inner_droppable_before_drop,
         text_outer_droppable_after_drop, text_inner_droppable_after_drop) = droppable_page.check_prevent_propogation('greedy outer')
        assert text_outer_droppable_before_drop == 'Outer droppable'
        assert text_inner_droppable_before_drop == 'Inner droppable (greedy)'
        assert text_outer_droppable_after_drop == 'Dropped!', 'Element has not been dropped'
        assert text_inner_droppable_after_drop == 'Inner droppable (greedy)'

    def test_revert_draggable(self, driver):
        droppable_page = DroppablePage(driver, 'https://demoqa.com/droppable')
        droppable_page.open_site()
        position_after_move_will, position_after_revert_will = droppable_page.check_revert_draggable('will')
        position_after_move_not_will, position_after_revert_not_will = droppable_page.check_revert_draggable('not will')
        assert position_after_move_will != position_after_revert_will, 'Element has not been reverted'
        assert position_after_move_not_will == position_after_revert_not_will, 'Element has been reverted'