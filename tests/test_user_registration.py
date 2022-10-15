import allure
from demoqa_tests.model.pages import registration_form

@allure.title("Заполнение формы регистрации студента")
def test_submit_student_details(setup_browser):
    browser = setup_browser
    registration_form.given_opened(browser)
    registration_form.given_opened(browser)

    with allure.step('Вводим данные для регистрации студента'):
        registration_form.set_first_name('Maria', browser)
        registration_form.set_last_name('Sklodowska', browser)
        registration_form.set_email('maria-sklodowska@gmail.com', browser)
        registration_form.set_gender('Female', browser)
        registration_form.set_phone_number('1234567890', browser)
        registration_form.set_date_of_birth([7, 'February', '2000'], browser)
        registration_form.set_subject('Physics', browser)
        registration_form.set_hobby('Music', browser)
        registration_form.set_picture('resources/picture.jpg', browser)
        registration_form.set_address('France, Paris', browser)

        registration_form.scroll_to_bottom(browser)
        registration_form.set_state('Haryana', browser)
        registration_form.set_city('Karnal', browser)

    with allure.step('Нажимаем кнопку submit'):
        registration_form.click_submit(browser)

    with allure.step('Проверяем корректность ранее введенных данных'):
        registration_form.should_have_submitted(
            [
                ('Student Name', 'Maria Sklodowska'),
                ('Student Email', 'maria-sklodowska@gmail.com'),
                ('Gender', 'Female'),
                ('Mobile', '1234567890'),
                ('Date of Birth', '07 February,2000'),
                ('Subjects', 'Physics'),
                ('Hobbies', 'Music'),
                ('Picture', 'picture.jpg'),
                ('Address', 'France, Paris'),
                ('State and City', 'Haryana Karnal')
            ], browser
        )




