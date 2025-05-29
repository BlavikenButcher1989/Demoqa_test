from dataclasses import dataclass

@dataclass
class Person:

    full_name: str
    firstname: str
    lastname: str
    age: int
    salary: int
    department: str
    email: str
    current_address: str
    permanent_address: str
    mobile: str


color_list = ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]

@dataclass
class Date:

    day: str
    month: str
    year: str
    time: str

menu_item_list = ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3']

options_to_select = ['Group 1, option 1', 'Group 1, option 2', 'Group 2, option 1', 'Group 2, option 2', 'A root option', 'Another root option', 'group 1, option 1', 'group 1, option 2', 'group 2, option 1', 'group 2, option 2', 'a root option', 'another root option']

titles_to_select = ['Dr.', 'Mr.', 'Mrs.', 'Ms.', 'Prof.', 'Other', 'dr.', 'mr.', 'mrs.', 'ms.', 'prof.', 'other']

drop_dawn_to_select = ['Green', 'Blue', 'Black', 'Red', 'green', 'blue', 'black', 'red']

old_select_menu = ['Red', 'Blue', 'Green', 'Yellow', 'Purple', 'Black', 'White', 'Voilet', 'Indigo', 'Magenta', 'Aqua']

standard_select_menu = ['Volvo', 'Saab', 'Opel', 'Audi']