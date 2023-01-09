# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/recover_passw_test.py

import time
import pytest

from config import TestData, ErrorMessage
from pages.recover_password_page import RecoverPassMethods
from pages.email_helper import EmailMethods



def test_UI_elements_recovery_passw_page(browser):
    """Тест 1. Проверка наличия основных элементов страницы восттановления пароля"""
    main_page = RecoverPassMethods(browser)
    main_page.get_main_page()
    main_page.click_on_forgot_pass_link()

    assert main_page.get_title_text()=='Восстановление пароля'
    assert main_page.phone_tab_is_visible()
    assert main_page.email_tab_is_visible()
    assert main_page.login_tab_is_visible()
    assert main_page.login_tab_is_visible()
    assert main_page.username_unput_is_visible()
    assert main_page.captcha_input_is_visible()
    assert main_page.continue_btn_is_visible()
    assert main_page.back_auth_btn_is_visible()


@pytest.mark.sms
@pytest.mark.captcha
def test_positive_recover_passw_phone(browser):
    '''Тест 2. Восстановление пароля по мобильному телефону'''
    # Заполнение формы восстановления пароля
    main_page = RecoverPassMethods(browser)
    main_page.get_main_page()
    main_page.click_on_forgot_pass_link()
    main_page.click_on_phone_swich()
    main_page.enter_username(TestData.valid_phone)

    # Время для ввода каптчи
    if main_page.captcha_is_visible():
        time.sleep(20)

    # Клик на кнопку "Продолжить"
    main_page.click_on_continue_button()

    # Время для ввода кода подтверждения
    if main_page.confirm_code_is_visible():
        time.sleep(20)

    # Ввод нового пароля и его подтверждение
    main_page.enter_new_password(TestData.password_2)
    main_page.enter_confirm_password(TestData.password_2)
    main_page.click_on_save_passw_btn()

    # Проверка, что восстановление прошло успешно и произошел переход на страницу авторизации
    assert 'Авторизация' == main_page.get_title_text()


@pytest.mark.captcha
def test_positive_recover_passw_email(positive_registration, browser):
    '''Тест 3. Восстановление пароля по электронной почте'''
    email_page = EmailMethods(browser)
    main_page = RecoverPassMethods(browser)

    # Получение адреса электронной почты
    email_adress = email_page.get_email()
    main_page.switch_to_first_window()
    # Заполнение формы восстановления пароля
    main_page.get_main_page()
    main_page.click_on_forgot_pass_link()
    main_page.click_on_email_swich()
    main_page.enter_username(email_adress)

    # Время для ввода каптчи
    if main_page.captcha_input_is_visible():
        time.sleep(30)

    # Клик на кнопку "Продолжить"
    main_page.click_on_continue_button()
    # Получение и ввод кода подтверждения           !!! По требованиям на почту должна приходить ссылка !!!
    #                                                       на форму восстановления пароля
    main_page.switch_new()
    email_page.open_recovery_email()
    conf_code = email_page.get_recovery_code()
    main_page.switch_to_first_window()
    main_page.enter_confirm_code(conf_code)
    # Ввод нового пароля и его подтверждение
    main_page.enter_new_password(TestData.password_2)
    main_page.enter_confirm_password(TestData.password_2)
    main_page.click_on_save_passw_btn()

    # Проверка, что восстановление прошло успешно и произошел переход на страницу авторизации
    assert 'Авторизация' == main_page.get_title_text()


@pytest.mark.captcha
def test_positive_recover_passw_resend_confcode(positive_registration, browser):
    '''Тест 4. Восстановление пароля по электронной почте с повторной отправкой кода подтверждения'''
    email_page = EmailMethods(browser)
    main_page = RecoverPassMethods(browser)

    # Получение адреса электронной почты
    email_adress = email_page.get_email()
    main_page.switch_to_first_window()
    # Заполнение формы восстановления пароля
    main_page.get_main_page()
    main_page.click_on_forgot_pass_link()
    main_page.click_on_email_swich()
    main_page.enter_username(email_adress)

    # Время для ввода каптчи
    if main_page.captcha_input_is_visible():
        time.sleep(20)

    # Клик на кнопку "Продолжить"
    main_page.click_on_continue_button()
    # Клик на кнопку повторной отправки кода подтверждения
    main_page.click_on_resend_code()
    # Получение и ввод кода подтверждения
    main_page.switch_new()
    email_page.open_recovery_email()
    conf_code = email_page.get_recovery_code()
    main_page.switch_to_first_window()
    main_page.enter_confirm_code(conf_code)
    # Ввод нового пароля и его подтверждение
    main_page.enter_new_password(TestData.password_2)
    main_page.enter_confirm_password(TestData.password_2)
    main_page.click_on_save_passw_btn()

    # Проверка, что восстановление прошло успешно и произошел переход на страницу авторизации
    assert 'Авторизация' == main_page.get_title_text()


@pytest.mark.captcha
def test_negative_recover_passw_wrong_conf_code(browser):
    '''Тест 5. Невозможность восстановления пароля с неверным кодом подтверждения'''
    main_page = RecoverPassMethods(browser)

    # Заполнение формы восстановления пароля
    main_page.get_main_page()
    main_page.click_on_forgot_pass_link()
    main_page.click_on_email_swich()
    main_page.enter_username(TestData.valid_email)

    # Время для ввода каптчи
    if main_page.captcha_input_is_visible():
        time.sleep(20)

    # Клик на кнопку "Продолжить"
    main_page.click_on_continue_button()
    # Ввод кода подтверждения
    main_page.enter_confirm_code(TestData.wrong_conf_code)

    # Проверка наличия подсказки о том, что код подтверждения неверный
    assert main_page.get_error_conf_code_text() == ErrorMessage.error_conf_code_message


@pytest.mark.captcha
@pytest.mark.parametrize("password", TestData.lst_invalid_passw, ids=TestData.ids_invalid_passw)
def test_negative_recovery_passw_wrong_new_passw_boundary_values(positive_registration, browser, password):
    '''Тест 6. Невозможность восстановления пароля с новым невалидным паролем'''

    # Присвоение переменным значений текста ошибки и пароля путем параметризации
    (error_message, passw) = password

    email_page = EmailMethods(browser)
    main_page = RecoverPassMethods(browser)

    # Получение адреса элетронной почты
    email_adress = email_page.get_email()
    main_page.switch_to_first_window()
    # Заполнение формы восстановления пароля
    main_page.get_main_page()
    main_page.click_on_forgot_pass_link()
    main_page.click_on_email_swich()
    main_page.enter_username(email_adress)

    # Время для ввода каптчи
    if main_page.captcha_input_is_visible():
        time.sleep(20)

    # Клик на кнопку "Продолжить"
    main_page.click_on_continue_button()
    # Получение и ввод кода подтверждения
    main_page.switch_new()
    email_page.open_recovery_email()
    conf_code = email_page.get_recovery_code()
    main_page.switch_to_first_window()
    main_page.enter_confirm_code(conf_code)
    # Ввод нового пароля и его подтверждение
    main_page.enter_new_password(passw)
    main_page.enter_confirm_password(passw)
    main_page.click_on_save_passw_btn()

    # Проверка наличия подсказки о том, что требуется ввести пользователю в поле пароль
    assert main_page.get_error_new_passw_text()==error_message