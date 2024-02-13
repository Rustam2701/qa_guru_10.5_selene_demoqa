from selene import browser, be, have, by, command
from test_demoqa_registration import image_resource


class RegistrationPage:
    def open(self):
        browser.open("/automation-practice-form")
        browser.all("[id^=google_ads][id$=container__]").with_(timeout=5).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all("[id^=google_ads][id$=container__]").perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def select_gender(self, value):
        browser.all("[name=gender]").element_by(have.value(value)).element("..").click()
        return self

    def fill_mobile_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def type_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value)
        browser.element('#react-select-2-option-0').click()
        browser.element('.subjects-auto-complete__multi-value__label').should(have.text(value))
        return self

    def select_hobbies(self, value):
        browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text(value)).click()
        return self

    def upload_picture(self, value):
        browser.element('#uploadPicture').set_value(image_resource.path(value))
        return self

    def input_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def select_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()
        return self

    def select_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def should_register_user_with(self, full_name, email, gender, number, date_of_birth, subjects, hobbies, photo,
                                  current_address, state_city):
        browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
        browser.element('.table').all('td').even.should(
            have.texts(
                full_name,
                email,
                gender,
                number,
                date_of_birth,
                subjects,
                hobbies,
                photo,
                current_address,
                state_city
            )
        )
