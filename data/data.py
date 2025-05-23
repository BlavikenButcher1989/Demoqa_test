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