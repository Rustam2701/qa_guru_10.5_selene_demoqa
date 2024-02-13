from test_demoqa_registration.pages.registration_page import RegistrationPage


def test_page_automation_form():
    registration_page = RegistrationPage()
    registration_page.open()

    (
        registration_page
            .fill_first_name("Светлана")
            .fill_last_name("Федоровна")
            .fill_email('bethere@example.com')
            .select_gender('Female')
            .fill_mobile_number('9866567667')
            .fill_date_of_birth('1993', 'May', '22')
            .type_subject('English')
            .select_hobbies('Sports')
            .upload_picture('111.png')
            .input_address('Ленина 139')
            .select_state("Haryana")
            .select_city('Karnal')
            .submit()
    )

    registration_page.should_register_user_with('Светлана Федоровна',
                                                'bethere@example.com',
                                                'Female',
                                                '9866567667',
                                                '22 May,1993',
                                                'English',
                                                'Sports',
                                                '111.png',
                                                'Ленина 139',
                                                'Haryana Karnal'
                                                )
