from selene import command
from selene.support.conditions import have
import files
from demoqa_tests.model.controls import dropdown, date_controls


def given_opened(browser):
    browser.open('http://demoqa.com/automation-practice-form')
    ads = browser.all('[id^=google_ads][id$=container__]')
    if ads.with_(timeout=10).wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)


def set_first_name(first_name, browser):
    browser.element('#firstName').type(first_name)


def set_last_name(last_name, browser):
    browser.element('#lastName').type(last_name)


def set_email(email, browser):
    browser.element('#userEmail').type(email)


def set_gender(gender, browser):
    if gender == 'Male':
        browser.element('.custom-control-label[for="gender-radio-1"]').click()
    elif gender == 'Female':
        browser.element('.custom-control-label[for="gender-radio-2"]').click()
    elif gender == 'Other':
        browser.element('.custom-control-label[for="gender-radio-3"]').click()


def set_phone_number(number, browser):
    browser.element('#userNumber').type(number)


def set_date_of_birth(date, browser):
    browser.element('#dateOfBirthInput').click()
    date_controls.select_month(date[1], browser)
    date_controls.select_year(date[2], browser)
    date_controls.select_day(date[1], date[0], browser)


def set_subject(value, browser):
    browser.element('#subjectsInput').type(value).press_enter()


def set_hobby(hobby, browser):
    if hobby == 'Sports':
        browser.element('.custom-control-label[for="hobbies-checkbox-1"]').click()
    elif hobby == 'Reading':
        browser.element('.custom-control-label[for="hobbies-checkbox-2"]').click()
    elif hobby == 'Music':
        browser.element('.custom-control-label[for="hobbies-checkbox-3"]').click()


def set_picture(path, browser):
    browser.element('#uploadPicture').send_keys(files.abs_path_from_project_root(path))


def set_address(address, browser):
    browser.element('#currentAddress').type(address)


def set_state(value: str, browser):
    dropdown.select(browser.element('#state'), value, browser)


def set_city(value: str, browser):
    dropdown.select(browser.element('#city'), value, browser)


def click_submit(browser):
    browser.element('#submit').perform(command.js.click)


def scroll_to_bottom(browser):
    browser.element('#state').perform(command.js.scroll_into_view)


def should_have_submitted(data, browser):
    rows = browser.element('.modal-content').all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))









