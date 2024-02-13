from selene import browser, be, have, by, command
from test_demoqa_registration import image_resource
from test_demoqa_registration.data.users_list import User


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all("[name=gender]")
        self.phone_number = browser.element('#userNumber')
        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.all('[for^=hobbies-checkbox]')
        self.picture = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.all('[id^=react-select][id*=option]')
        self.city = browser.all('[id^=react-select][id*=option]')

    def open(self):
        browser.open("/automation-practice-form")
        browser.all("[id^=google_ads][id$=container__]").with_(timeout=5).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all("[id^=google_ads][id$=container__]").perform(command.js.remove)

    def fill_first_name(self, user: User):
        self.first_name.type(user.first_name)
        return self

    def fill_last_name(self, user: User):
        self.last_name.type(user.last_name)
        return self

    def fill_email(self, user: User):
        self.email.type(user.email)
        return self

    def select_gender(self, user: User):
        self.gender.element_by(have.value(user.gender)).element("..").click()
        return self

    def fill_mobile_number(self, user: User):
        self.phone_number.type(user.phone_number)
        return self

    def fill_date_of_birth(self, user: User):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').send_keys(user.date_of_birth_year)
        browser.element('.react-datepicker__month-select').send_keys(user.date_of_birth_month)
        browser.element(f'.react-datepicker__day--0{user.date_of_birth_day}').click()
        return self

    def type_subject(self, user: User):
        self.subjects.should(be.blank).type(user.subjects)
        browser.element('#react-select-2-option-0').click()
        browser.element('.subjects-auto-complete__multi-value__label').should(have.text(user.subjects))
        return self

    def select_hobbies(self, user: User):
        self.hobbies.element_by(have.exact_text(user.hobbies)).click()
        return self

    def upload_picture(self, user: User):
        self.picture.set_value(image_resource.path(user.picture))
        return self

    def input_address(self, user: User):
        self.current_address.type(user.current_address)
        return self

    def select_state(self, user: User):
        browser.element('#state').click()
        self.state.element_by(have.exact_text(user.state)).click()
        return self

    def select_city(self, user: User):
        browser.element('#city').click()
        self.city.element_by(have.exact_text(user.city)).click()
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def user_registration(self, user: User):
        self.fill_first_name(user) \
            .fill_last_name(user) \
            .fill_email(user) \
            .select_gender(user) \
            .fill_mobile_number(user) \
            .fill_date_of_birth(user) \
            .type_subject(user) \
            .select_hobbies(user) \
            .upload_picture(user) \
            .input_address(user) \
            .select_state(user) \
            .select_city(user) \
            .submit()

    def should_register_user_with(self, user: User):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(
            have.texts(
                f'{user.first_name} {user.last_name}',
                {user.email},
                {user.gender},
                {user.phone_number},
                f'{user.date_of_birth_day} {user.date_of_birth_month},{user.date_of_birth_year}',
                {user.subjects},
                {user.hobbies},
                {user.picture},
                {user.current_address},
                f'{user.state} {user.city}',
            )
        )
