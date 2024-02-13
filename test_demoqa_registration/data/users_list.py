import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth_year: str
    date_of_birth_month: str
    date_of_birth_day: str
    subjects: str
    hobbies: str
    picture: str
    current_address: str
    state: str
    city: str


svetlana = User(
    first_name='Светлана',
    last_name='Федоровна',
    email='bethere@example.com',
    gender='Female',
    phone_number='9866567667',
    date_of_birth_year='1993',
    date_of_birth_month='May',
    date_of_birth_day='22',
    subjects='English',
    hobbies='Sports',
    picture='111.png',
    current_address='Ленина 139',
    state='Haryana',
    city='Karnal',
)
