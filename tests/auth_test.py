# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/auth_test.py

import time

from config import TestData, ErrorMessage
from pages.auth_page import AuthMethods


def test_UI_elements_auth_page(browser):
    '''Тест 1. Проверка наличия основных элементов страницы Авторизации'''
    main_page = AuthMethods(browser)
    main_page.get_main_page()
    main_page.click_on_email_swich()

    assert main_page.get_title_text()=='Авторизация'
    assert main_page.rt_title_is_visible()
    assert main_page.phone_tab_is_visible()
    assert main_page.email_tab_is_visible()
    assert main_page.login_tab_is_visible()
    assert main_page.login_tab_is_visible()
    assert main_page.username_input_is_visible()
    assert main_page.passsw_input_is_visible()
    assert main_page.auth_btn_is_visible()
    assert main_page.reg_btn_is_visible()

def test_positive_auth_email(browser):
    '''Тест 2. Авторизация зарегистрированного пользователя по email с валидным паролем, вкладка Почта'''
    # Заполнение формы авторизации
    main_page = AuthMethods(browser)
    main_page.get_main_page()
    main_page.click_on_email_swich()
    main_page.enter_username(TestData.valid_email)
    main_page.enter_password(TestData.password_1)
    main_page.click_on_checkbox()

    # время для ввода каптчи
    if main_page.captcha_is_visible:
        time.sleep(15)

    # Клик по кнопке регистрации
    main_page.click_on_auth_button()

    # Проверка, что авторизаия прошла успешно и произошел переход в личный кабинет
    assert main_page.pers_acc_is_visible()


def test_positive_auth_phone(browser):
    '''Тест 3. Авторизация зарегистрированного пользователя по мобильному телефону с валидным паролем, вкладка Номер'''
    # Заполнение формы авторизации
    main_page = AuthMethods(browser)
    main_page.get_main_page()
    main_page.click_on_phone_swich()
    main_page.enter_username(TestData.valid_phone)
    main_page.enter_password(TestData.password_1)
    main_page.click_on_checkbox()

    # время для ввода каптчи
    if main_page.captcha_is_visible:
        time.sleep(15)

    # Клик по кнопке регистрации
    main_page.click_on_auth_button()

    # Проверка, что авторизаия прошла успешно и произошел переход в личный кабинет
    assert main_page.pers_acc_is_visible()


def test_negative_auth_wrong_passw(browser):
    '''Тест 4. Невозможность авторизации по email с неверным паролем'''
    # Заполнение формы авторизации
    main_page = AuthMethods(browser)
    main_page.get_main_page()
    main_page.click_on_email_swich()
    main_page.enter_username(TestData.valid_email)
    main_page.enter_password(TestData.wrong_password)
    main_page.click_on_checkbox()

    # время для ввода каптчи
    if main_page.captcha_is_visible:
        time.sleep(15)

    # Клик по кнопке регистрации
    main_page.click_on_auth_button()

    # Проверка наличия сообщения о неверном логине или пароле
    assert main_page.error_message_login_is_visible()
    # Проверка, что кнопка "Забыли пароль" стала оранжевой
    assert main_page.color_of_text_fogot_pw() == 'rgba(255, 79, 18, 1)'

def test_negative_auth_no_user(browser):
    '''Тест 5. Невозможность авторизации незарегистрированного в системе пользователя'''
    # Заполнение формы авторизации
    main_page = AuthMethods(browser)
    main_page.get_main_page()
    main_page.click_on_email_swich()
    main_page.enter_username(TestData.no_register_email)
    main_page.enter_password(TestData.password_1)
    main_page.click_on_checkbox()

    # время для ввода каптчи
    if main_page.captcha_is_visible:
        time.sleep(15)

    # Клик по кнопке регистрации
    main_page.click_on_auth_button()

    # Проверка наличия сообщения о неверном логине или пароле
    assert main_page.error_message_login_is_visible()
    # Проверка, что кнопка "Забыли пароль" стала оранжевой
    assert main_page.color_of_text_fogot_pw() == 'rgba(255, 79, 18, 1)'


def test_negative_auth_empty_email(browser):
    '''Тест 6. Невозможность авторизации по email с пустым полем "Электронная почта" '''
    # Заполнение формы авторизации
    main_page = AuthMethods(browser)
    main_page.get_main_page()
    main_page.click_on_email_swich()
    main_page.enter_username(TestData.empty)
    main_page.enter_password(TestData.password_1)
    main_page.click_on_checkbox()

    # время для ввода каптчи
    if main_page.captcha_is_visible:
        time.sleep(15)

    # Клик по кнопке регистрации
    main_page.click_on_auth_button()

    # Проверка наличия подсказки о необходимости заполнить поле Электронная почта
    assert main_page.get_error_username_text()==ErrorMessage.error_email_message


def test_negative_auth_empty_passw(browser):
    '''Тест 7. Невозможность авторизации по email с пустым полем "Пароль"'''
    # Заполнение формы авторизации
    main_page = AuthMethods(browser)
    main_page.get_main_page()
    main_page.click_on_email_swich()
    main_page.enter_username(TestData.valid_email)
    main_page.enter_password(TestData.wrong_password)
    main_page.click_on_checkbox()

    # время для ввода каптчи
    if main_page.captcha_is_visible:
        time.sleep(15)

    # Клик по кнопке регистрации
    main_page.click_on_auth_button()

    # Проверка наличия сообщения о неверном логине или пароле
    assert main_page.error_message_login_is_visible()
    # Проверка, что кнопка "Забыли пароль" стала оранжевой
    assert main_page.color_of_text_fogot_pw() == 'rgba(255, 79, 18, 1)'


