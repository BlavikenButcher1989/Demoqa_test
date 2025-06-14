import random
import time

from pages.base_page import BasePage
from locators.interactions_locators import SortablePageLocators
from locators.interactions_locators import SelectablePageLocators
from locators.interactions_locators import ResizablePageLocators

class SortablePage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.elements_are_visible(elements)

        return [item.text for item in item_list]

    def change_list_order(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        order_before = self.get_sortable_items(self.locators.LIST_ITEMS)
        item_list = random.sample(self.elements_are_visible(self.locators.LIST_ITEMS), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.drag_and_drop_elements(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.LIST_ITEMS)

        return order_before, order_after

    def change_grid_order(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        order_before = self.get_sortable_items(self.locators.GRID_ITEMS)
        item_grid = random.sample(self.elements_are_visible(self.locators.GRID_ITEMS), k=2)
        item_what = item_grid[0]
        item_where = item_grid[1]
        self.drag_and_drop_elements(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.GRID_ITEMS)

        return order_before, order_after

class SelectablePage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = SelectablePageLocators()

    def click_elements(self, elements):
        count_items = 0
        items_list = random.sample(self.elements_are_visible(elements),
                                   random.randint(1, len(self.elements_are_visible(elements))))
        for item in items_list:
            item.click()
            count_items += 1

        return count_items

    def change_list_order(self):
        self.element_is_visible(self.locators.TAB_LIST).click()
        count_item = self.click_elements(self.locators.LIST_ITEM)
        item_list_active = self.elements_are_visible(self.locators.LIST_ITEM_ACTIVE)

        return count_item, len(item_list_active)

    def change_grid_order(self):
        self.element_is_visible(self.locators.TAB_GRID).click()
        count_item = self.click_elements(self.locators.GRID_ITEM)
        item_grid_active = self.elements_are_visible(self.locators.GRID_ITEM_ACTIVE)

        return count_item, len(item_grid_active)

class ResizablePage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = ResizablePageLocators()

    def get_px_from_width_height(self, value_size):
        width = value_size.split(';')[0].split(':')[1].replace(' ', '')[:-2]
        height = value_size.split(';')[1].split(':')[1].replace(' ', '')[:-2]

        return width, height

    def get_max_min_size(self, element):
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')

        return size_value

    def change_size_resizable_box(self):
        element = self.element_is_clickable(self.locators.RESIZABLE_BOX_HANDLE)
        self.action_move_to_element(element)
        self.slide_drag_and_drop(element, 400, 300)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))

        element = self.element_is_clickable(self.locators.RESIZABLE_BOX_HANDLE)
        self.action_move_to_element(element)
        self.slide_drag_and_drop(element, -400, -200)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))

        return ", ".join(map(str, max_size)), ", ".join(map(str, min_size))

    def change_size_resizable(self):
        element = self.element_is_clickable(self.locators.RESIZABLE_HANDLE)
        self.action_move_to_element(element)
        self.slide_drag_and_drop(element, random.randint(1, 300), random.randint(1,300))
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))

        element = self.element_is_clickable(self.locators.RESIZABLE_HANDLE)
        self.action_move_to_element(element)
        self.slide_drag_and_drop(element, random.randint(-200, 1), random.randint(-200, 1))
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))

        return max_size, min_size