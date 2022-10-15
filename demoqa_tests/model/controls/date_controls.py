from selene import command
from selene.support.conditions import have


def select_month(month, browser):
    browser.element('.react-datepicker__month-select').click()
    browser.all('.react-datepicker__month-select option').by(have.exact_text(month)).first.click()


def select_year(year, browser):
    browser.element('.react-datepicker__year-select').click()
    element_year = browser.all('.react-datepicker__year-select option').by(have.exact_text(year)).first
    element_year.perform(command.js.scroll_into_view)
    element_year.click()


def select_day(month, day, browser):
    browser.element(f'[aria-label*="{month} {day}"]').click()


def type_date(date, browser):
    browser.element('#dateOfBirthInput').type(date)




