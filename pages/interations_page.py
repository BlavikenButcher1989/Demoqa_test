import random
import re
import time

from pages.base_page import BasePage
from locators.interactions_locators import SortablePageLocators
from locators.interactions_locators import SelectablePageLocators
from locators.interactions_locators import ResizablePageLocators
from locators.interactions_locators import DroppablePageLocators
from locators.interactions_locators import DraggablePageLocators

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

class DroppablePage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = DroppablePageLocators()

    def check_simple(self):
        self.element_is_visible(self.locators.BUTTON_SIMPLE).click()
        drag_me = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_here = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        text_before_drop = drop_here.text
        self.drag_and_drop_elements(drag_me, drop_here)
        text_after_drop = drop_here.text

        return text_before_drop, text_after_drop

    def check_acceptable(self):
        self.element_is_visible(self.locators.BUTTON_ACCEPT).click()
        acceptable = self.element_is_visible(self.locators.ACCEPTABLE)
        drop_here = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        text_before_drop = drop_here.text
        self.drag_and_drop_elements(acceptable, drop_here)
        text_after_drop = drop_here.text

        return text_before_drop, text_after_drop

    def check_not_acceptable(self):
        self.element_is_visible(self.locators.BUTTON_ACCEPT).click()
        not_acceptable = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_here = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        text_before_drop = drop_here.text
        self.drag_and_drop_elements(not_acceptable, drop_here)
        text_after_drop = drop_here.text

        return text_before_drop, text_after_drop

    def check_prevent_propogation(self, drop_box):

        self.element_is_visible(self.locators.BUTTON_PREVENT_PROPOGATION).click()
        drag_me = self.element_is_visible(self.locators.DRAG_ME_PREVENT_PROPOGATION)
        boxes_list = {
            'not greedy': {
                'outer_droppable': self.element_is_visible(self.locators.NOT_GREEDY_OUTER_DROPPABLE),
                'inner_droppable': self.element_is_visible(self.locators.NOT_GREEDY_INNER_DROPPABLE)
            },
            'greedy': {
                'outer_droppable': self.element_is_visible(self.locators.GREEDY_OUTER_DROPPABLE),
                'inner_droppable': self.element_is_visible(self.locators.GREEDY_INNER_DROPPABLE)
            }
        }

        if drop_box == 'not greedy':
            text_outer_droppable_before_drop = boxes_list['not greedy']['outer_droppable'].text
            text_inner_droppable_before_drop = boxes_list['not greedy']['inner_droppable'].text
            self.drag_and_drop_elements(drag_me, boxes_list['not greedy']['inner_droppable'])
            text_outer_droppable_after_drop = boxes_list['not greedy']['outer_droppable'].text
            text_inner_droppable_after_drop = boxes_list['not greedy']['inner_droppable'].text

            return text_outer_droppable_before_drop, text_inner_droppable_before_drop, text_outer_droppable_after_drop, text_inner_droppable_after_drop

        if drop_box == 'greedy inner':
            text_outer_droppable_before_drop = boxes_list['greedy']['outer_droppable'].text
            text_inner_droppable_before_drop = boxes_list['greedy']['inner_droppable'].text
            self.drag_and_drop_elements(drag_me, boxes_list['greedy']['inner_droppable'])
            text_outer_droppable_after_drop = boxes_list['greedy']['outer_droppable'].text
            text_inner_droppable_after_drop = boxes_list['greedy']['inner_droppable'].text

            return text_outer_droppable_before_drop, text_inner_droppable_before_drop, text_outer_droppable_after_drop, text_inner_droppable_after_drop

        if drop_box == 'greedy outer':
            text_outer_droppable_before_drop = boxes_list['greedy']['outer_droppable'].text
            text_inner_droppable_before_drop = boxes_list['greedy']['inner_droppable'].text
            self.drag_and_drop_elements(drag_me, boxes_list['greedy']['outer_droppable'])
            text_outer_droppable_after_drop = boxes_list['greedy']['outer_droppable'].text
            text_inner_droppable_after_drop = boxes_list['greedy']['inner_droppable'].text

            return text_outer_droppable_before_drop, text_inner_droppable_before_drop, text_outer_droppable_after_drop, text_inner_droppable_after_drop

    def check_revert_draggable(self, type_drag):

        self.element_is_visible(self.locators.BUTTON_REVERT_DRAGGABLE).click()

        drags = {
            'will': self.element_is_visible(self.locators.WILL_REVERT),
            'not will': self.element_is_visible(self.locators.NOT_REVERT),
            'drop_here': self.element_is_visible(self.locators.DROP_HERE_REVERT_DRAGGABLE)
        }

        revert = drags[type_drag]
        drop_here = drags['drop_here']
        self.drag_and_drop_elements(revert, drop_here)
        position_after_move = revert.get_attribute('style')
        time.sleep(0.5)
        position_after_revert = revert.get_attribute('style')

        return position_after_move, position_after_revert

class DraggablePage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver, url)

    locators = DraggablePageLocators()

    def check_simple(self):
        self.element_is_visible(self.locators.BUTTON_SIMPLE).click()
        drag_me = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        position_before = drag_me.get_attribute('style')
        self.slide_drag_and_drop(drag_me, random.randint(1, 200), random.randint(1, 200))
        position_after = drag_me.get_attribute('style')

        return position_before, position_after

    def get_position(self, element):
        position = re.findall(r"\d+\.\d+|\d+", element)

        return position

    def check_axis_restricted(self, coord):
        self.element_is_visible(self.locators.BUTTON_AXIS_RESTRICTED).click()

        coordinates = {
            'only_x': self.element_is_visible(self.locators.ONLY_X),
            'only_y': self.element_is_visible(self.locators.ONLY_Y)
        }

        element = coordinates[coord]
        self.slide_drag_and_drop(element, random.randint(-100, 100), random.randint(-100, 100))
        position_after_move = self.get_position(element.get_attribute('style'))

        return [int(dig) for dig in position_after_move]

    def check_container_restricted(self, cont):
        self.element_is_visible(self.locators.BUTTON_CONTAINER_RESTRICTED).click()
        contained = {
            'box': self.element_is_visible(self.locators.WITHIN_BOX),
            'parent': self.element_is_visible(self.locators.WITHIN_PARENT)
        }

        element = contained[cont]
        self.slide_drag_and_drop(element, 900, 120)
        position_after_move = self.get_position(element.get_attribute('style'))

        return [float(dig) for dig in position_after_move]