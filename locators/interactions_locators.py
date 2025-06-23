from selenium.webdriver.common.by import By

class SortablePageLocators:

    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_ITEMS = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')

    TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEMS = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')

class SelectablePageLocators:

    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_ITEM = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item list-group-item-action"]')
    LIST_ITEM_ACTIVE = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item active list-group-item-action"]')

    TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEM = (By.CSS_SELECTOR, 'li[class="list-group-item list-group-item-action"]')
    GRID_ITEM_ACTIVE = (By.CSS_SELECTOR, 'li[class="list-group-item active list-group-item-action"]')

class ResizablePageLocators:

    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR, 'div[class="constraint-area"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, 'div[id="resizable"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE = (By.CSS_SELECTOR, 'div[id="resizable"]')

class DroppablePageLocators:

    # Simple tab
    BUTTON_SIMPLE = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-simple"]')
    DRAG_ME_SIMPLE = (By.CSS_SELECTOR, 'div[id="draggable"]')
    DROP_HERE_SIMPLE = (By.CSS_SELECTOR, 'div[id="simpleDropContainer"] div[id="droppable"]')

    # Accept tab
    BUTTON_ACCEPT = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="notAcceptable"]')
    DROP_HERE_ACCEPT = (By.CSS_SELECTOR, 'div[id="acceptDropContainer"] div[id="droppable"]')

    # Prevent propogation tab
    BUTTON_PREVENT_PROPOGATION = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-preventPropogation"]')
    DRAG_ME_PREVENT_PROPOGATION = (By.CSS_SELECTOR, 'div[id="dragBox"]')
    # Not greedy
    NOT_GREEDY_OUTER_DROPPABLE = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"] p:nth-child(1)')
    NOT_GREEDY_INNER_DROPPABLE = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    # Greedy
    GREEDY_OUTER_DROPPABLE = (By.CSS_SELECTOR, 'div[id="greedyDropBox"] p:nth-child(1)')
    GREEDY_INNER_DROPPABLE = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')

    # Revert draggable tab
    BUTTON_REVERT_DRAGGABLE = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-revertable"]')
    WILL_REVERT = (By.CSS_SELECTOR, 'div[id="revertable"]')
    NOT_REVERT = (By.CSS_SELECTOR, 'div[id="notRevertable"]')
    DROP_HERE_REVERT_DRAGGABLE = (By.CSS_SELECTOR, 'div[id="revertableDropContainer"] div[id="droppable"]')

class DraggablePageLocators:

    # Simple
    BUTTON_SIMPLE = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-simple"]')
    DRAG_ME_SIMPLE = (By.CSS_SELECTOR, 'div[id="dragBox"]')

    # Axis Restricted
    BUTTON_AXIS_RESTRICTED = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-axisRestriction"]')
    ONLY_X = (By.CSS_SELECTOR, 'div[id="restrictedX"]')
    ONLY_Y = (By.CSS_SELECTOR, 'div[id="restrictedY"]')

    # Container Restricted
    BUTTON_CONTAINER_RESTRICTED = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-containerRestriction"]')
    WITHIN_BOX = (By.CSS_SELECTOR, 'div[class="draggable ui-widget-content ui-draggable ui-draggable-handle"]')
    WITHIN_PARENT = (By.CSS_SELECTOR, 'span[class="ui-widget-header ui-draggable ui-draggable-handle"]')