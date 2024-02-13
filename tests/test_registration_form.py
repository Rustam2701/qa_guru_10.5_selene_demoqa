from test_demoqa_registration.data import users_list
from test_demoqa_registration.pages.registration_page import RegistrationPage


def test_page_automation_form_2():
    registration_page = RegistrationPage()
    user1 = users_list.svetlana
    registration_page.open()
    registration_page.user_registration(user1)
    registration_page.should_register_user_with(user1)
