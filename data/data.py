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