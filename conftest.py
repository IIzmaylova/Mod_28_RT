import pytest
from selenium import webdriver


from config import TestData as TD
from pages.register_page import RegisterMethods
from pages.email_helper import EmailMethods


# Фикстура для запуска браузера, запускается с каждым тестом
@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    yield driver
    driver.quit()

@pytest.fixture()
def positive_registration(browser):
    email_page = EmailMethods(browser)
    registration = RegisterMethods(browser)
    # Получение уникального адреса электронной почты
    email_page.go_to_mail()
    email_adress = email_page.get_email()
    # Заполнение анкеты регистрации
    registration.fill_out_registr_form(TD.first_name_positive1, TD.last_name_positive1, email_adress, TD.password_1)
    # Получение и ввод кода подтверждение по электронной почте
    registration.switch_new()
    email_page.open_last_email()
    confirm_code = email_page.get_registration_code()
    email_page.click_on_back_email()
    # Ввод кода подтверждения
    registration.switch_to_first_window()
    registration.enter_confirm_code(confirm_code)
    registration.click_on_logout_btn()
    registration.switch_new()






