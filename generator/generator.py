import random

from data.data import Person, Date

from faker import Faker

faker_ru = Faker('ru_Ru')
faker_en = Faker('En')


def generator_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(20000, 80000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn()[:10]
    )


def generated_file():
    file_name = f'filetest{random.randint(0, 999)}.txt'
    path = rf'C:\PycharmProjects\Demoqa_test\{file_name}'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file_name, path


def generator_subjects():
    subjects = ['Hindi', 'English', 'Maths', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'Commerce',
                'Accounting', 'Economics', 'Arts', 'Social Studies', 'History', 'Civics']
    return random.choice(subjects)


def generator_states():
    states = ['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']
    return random.choice(states)


def generator_cities():
    ncr = ['Delhi', 'Gurgaon', 'Noida']
    uttar_Pradesh = ['Agra', 'Lucknow', 'Merrut']
    haryana = ['Karnal', 'Panipat']
    rajasthan = ['Jaipur', 'Jaiselmer']
    state = generator_states()
    if state == 'NCR':
        return state, random.choice(ncr)
    if state == 'Uttar Pradesh':
        return state, random.choice(uttar_Pradesh)
    if state == 'Haryana':
        return state, random.choice(haryana)
    if state == 'Rajasthan':
        return state, random.choice(rajasthan)


def generator_month_and_year():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    month_dict = {'January': '0', 'February': '1', 'March': '2', 'April': '3', 'May': '4', 'June': '5', 'July': '6',
                  'August': '7', 'September': '8', 'October': '9', 'November': '10', 'December': '11'}
    month_dict_revers = {'0': 'January', '1': 'February', '2': 'March', '3': 'April', '4': 'May', '5': 'June',
                         '6': 'July', '7': 'August', '8': 'September', '9': 'October', '10': 'November',
                         '11': 'December'}
    month_value = month_dict[random.choice(months)]
    month = month_dict_revers[month_value]
    year = random.randint(1900, 2025)

    return month, month_value, str(year)

def generator_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time='12:00'
    )