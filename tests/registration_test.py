# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/registration_test.py

import time
import pytest

from config import TestData, ErrorMessage
from pages.register_page import RegisterMethods
from pages.email_helper import EmailMethods


def test_UI_elements_registr_page(browser):
    '''Тест 1. Проверка наличия основных элементов страницы Авторизации'''
    main_page = RegisterMethods(browser)
    main_page.get_main_page()
    main_page.click_on_registration_link()

    assert main_page.get_title_text()=='Регистрация'
    assert main_page.rt_title_is_visible()
    assert main_page.firstname_input_is_visible()
    assert main_page.lastname_input_is_visible()
    assert main_page.region_is_visible()
    assert main_page.adress_input_is_visible()
    assert main_page.password_input_is_visible()
    assert main_page.conf_password_input_is_visible()
    assert main_page.reg_btn_is_visible()


def test_positive_registration_email(browser):
    '''Тест 2. Регистрация с валидными данными через Email'''
    # Получение уникального адреса электронной почты
    email_page = EmailMethods(browser)
    email_page.go_to_mail()
    email_adress = email_page.get_email()

    # Заполнение анкеты регистрации
    main_page = RegisterMethods(browser)
    main_page.switch_to_first_window()
    main_page.get_main_page()
    main_page.click_on_registration_link()
    main_page.enter_firstname(TestData.first_name_positive1)
    main_page.enter_lastname(TestData.last_name_positive1)
    main_page.enter_adress(email_adress)
    main_page.enter_password(TestData.password_1)
    main_page.enter_conf_passw(TestData.password_1)
    main_page.click_on_registration_btn()

    # Получение кода подтверждение по электронной почте
    email_page.switch_new()
    email_page.open_last_email()
    conf_code = email_page.get_registration_code()

    # Ввод кода подтверждения
    main_page.switch_to_first_window()
    main_page.enter_confirm_code(conf_code)

    # Проверка, что регистрация прошла успешна и произошел переход в личный кабинет
    assert main_page.pers_acc_is_visible()

@pytest.mark.sms
def test_positive_registration_phone(browser):
    '''Тест 3. Регистрация с валидными данными через Телефон'''
    # Заполнение анкеты регистрации
    main_page = RegisterMethods(browser)
    main_page.get_main_page()
    main_page.click_on_registration_link()
    main_page.enter_firstname(TestData.first_name_positive1)
    main_page.enter_lastname(TestData.last_name_positive1)
    main_page.enter_adress(TestData.valid_phone)
    main_page.enter_password(TestData.password_1)
    main_page.enter_conf_passw(TestData.password_1)
    main_page.click_on_registration_btn()

    # Время для ввода кода подтверждения
    if main_page.confirm_code_is_visible():
        time.sleep(15)
    # Проверка, что регистрация прошла успешна и произошел переход в личный кабинет
    assert main_page.pers_acc_is_visible()


@pytest.mark.parametrize("firstname", TestData.lst_valid_firstname, ids=TestData.ids_valid_name)
def test_positive_registration_firstname_boundary_values(browser, firstname):
    '''Тест 4. Регистрация с валидным именем. КЭ и ГЗ'''
    # Получение уникального адреса электронной почты
    email_page = EmailMethods(browser)
    email_page.go_to_mail()
    email_adress = email_page.get_email()

    # Заполнение анкеты регистрации
    main_page = RegisterMethods(browser)
    main_page.switch_to_first_window()
    main_page.get_main_page()
    main_page.click_on_registration_link()
    main_page.enter_firstname(firstname)
    main_page.enter_lastname(TestData.last_name_positive1)
    main_page.enter_adress(email_adress)
    main_page.enter_password(TestData.password_1)
    main_page.enter_conf_passw(TestData.password_1)
    main_page.click_on_registration_btn()

    # Получение кода подтверждение по электронной почте
    email_page.switch_new()
    email_page.open_last_email()
    conf_code = email_page.get_registration_code()

    # Ввод кода подтверждения
    main_page.switch_to_first_window()
    main_page.enter_confirm_code(conf_code)

    # Проверка, что регистрация прошла успешна и произошел переход в личный кабинет
    assert main_page.pers_acc_is_visible()


@pytest.mark.parametrize("lastname", TestData.lst_valid_lastname, ids=TestData.ids_valid_name)
def test_positive_registration_lastname_boundary_values(browser, lastname):
    '''Тест 5. Регистрация с валидной фамилией. КЭ и ГЗ'''
    # Получение уникального адреса электронной почты
    email_page = EmailMethods(browser)
    email_page.go_to_mail()
    email_adress = email_page.get_email()

    # Заполнение анкеты регистрации
    main_page = RegisterMethods(browser)
    main_page.switch_to_first_window()
    main_page.get_main_page()
    main_page.click_on_registration_link()
    main_page.enter_firstname(TestData.first_name_positive1)
    main_page.enter_lastname(lastname)
    main_page.enter_adress(email_adress)
    main_page.enter_password(TestData.password_1)
    main_page.enter_conf_passw(TestData.password_1)
    main_page.click_on_registration_btn()

    # Получение кода подтверждение по электронной почте
    email_page.switch_new()
    email_page.open_last_email()
    conf_code = email_page.get_registration_code()

    # Ввод кода подтверждения
    main_page.switch_to_first_window()
    main_page.enter_confirm_code(conf_code)

    # Проверка, что регистрация прошла успешна и произошел переход в личный кабинет
    assert main_page.pers_acc_is_visible()


@pytest.mark.parametrize("password", TestData.lst_valid_passw, ids=TestData.ids_valid_passw)
def test_positive_registration_password_boundary_values(browser, password):
    '''Тест 6. Регистрация с валидным паролем. КЭ и ГЗ'''
    # Получение уникального адреса электронной почты
    email_page = EmailMethods(browser)
    email_page.go_to_mail()
    email_adress = email_page.get_email()

    # Заполнение анкеты регистрации
    main_page = RegisterMethods(browser)
    main_page.switch_to_first_window()
    main_page.get_main_page()
    main_page.click_on_registration_link()
    main_page.enter_firstname(TestData.first_name_positive1)
    main_page.enter_lastname(TestData.lst_valid_lastname)
    main_page.enter_adress(email_adress)
    main_page.enter_password(password)
    main_page.enter_conf_passw(password)
    main_page.click_on_registration_btn()

    # Получение кода подтверждение по электронной почте
    email_page.switch_new()
    email_page.open_last_email()
    conf_code = email_page.get_registration_code()

    # Ввод кода подтверждения
    main_page.switch_to_first_window()
    main_page.enter_confirm_code(conf_code)
    # Проверка, что регистрация прошла успешна и произошел переход в личный кабинет
    assert main_page.pers_acc_is_visible()


def test_negative_registration_no_unic_phone(browser):
    '''Тест 7. Невозможность регистрации через телефон, уже зарегистрированный в системе'''
    # Заполнение анкеты регистрации
    main_page = RegisterMethods(browser)
    main_page.get_main_page()
    main_page.click_on_registration_link()
    main_page.enter_firstname(TestData.first_name_positive1)
    main_page.enter_lastname(TestData.last_name_positive1)
    main_page.enter_adress(TestData.no_unic_phone)
    main_page.enter_password(TestData.password_1)
    main_page.enter_conf_passw(TestData.password_1)
    main_page.click_on_registration_btn()

    # Проверка того, что появилось модальное окно с предупреждением о том,
    # что пользователь с таким телефоном уже зарегистрирован в системе
    assert main_page.this_username_exists_is_visible()


def test_negative_registration_no_unic_email(browser):
    '''Тест 8. Невозможность регистрации через email, уже зарегистрированный в системе'''
    # Заполнение анкеты регистрации
    main_page = RegisterMethods(browser)
    main_page.get_main_page()
    main_page.click_on_registration_link()
    main_page.enter_firstname(TestData.first_name_positive1)
    main_page.enter_lastname(TestData.last_name_positive1)
    main_page.enter_adress(TestData.no_unic_mail)
    main_page.enter_password(TestData.password_1)
    main_page.enter_conf_passw(TestData.password_1)
    main_page.click_on_registration_btn()

    # Проверка того, что появилось модальное окно с предупреждением о том,
    # что пользователь с таким телефоном уже зарегистрирован в системе
    assert main_page.this_username_exists_is_visible()


@pytest.mark.parametrize("firstname", TestData.lst_invalid_name, ids=TestData.ids_invalid_name)
def test_negativ_registration_firstname_boundary_values(browser, firstname):
    '''Тест 9. Невозможность регистрации с невалидным именем. КЭ и ГЗ'''
    # Заполнение анкеты регистрации
    main_page = RegisterMethods(browser)
    main_page.get_main_page()
    main_page.click_on_registration_link()
    main_page.enter_firstname(firstname)
    main_page.enter_lastname(TestData.first_name_positive1)
    main_page.enter_adress(TestData.no_register_email)
    main_page.enter_password(TestData.password_1)
    main_page.enter_conf_passw(TestData.password_1)
    main_page.click_on_registration_btn()

    # Проверка наличия подсказки о том, что должен ввести пользователь в поле
    assert main_page.get_error_firstname_text()==ErrorMessage.error_firstname_message


@pytest.mark.parametrize("lastname", TestData.lst_invalid_name, ids=TestData.ids_invalid_name)
def test_negative_registration_lastname_boundary_values(browser, lastname):
    '''Тест 10. Невозможность регистрации с невалидной фамилией. КЭ и ГЗ'''
    # Заполнение анкеты регистрации
    main_page = RegisterMethods(browser)
    main_page.get_main_page()
    main_page.click_on_registration_link()
    main_page.enter_firstname(TestData.first_name_positive1)
    main_page.enter_lastname(lastname)
    main_page.enter_adress(TestData.no_register_email)
    main_page.enter_password(TestData.password_1)
    main_page.enter_conf_passw(TestData.password_1)
    main_page.click_on_registration_btn()

    # Проверка наличия подсказки о том, что должен ввести пользователь в поле
    assert main_page.get_error_lastname_text()==ErrorMessage.error_lastname_message


@pytest.mark.parametrize("adress", TestData.lst_invalid_name, ids=TestData.ids_invalid_name)
def test_negative_registration_adress_boundary_values(browser, adress):
    '''Тест 11. Невозможность регистрации с невалидным номером телефона или электронной почтой. КЭ и ГЗ'''
    # Заполнение анкеты регистрации
    main_page = RegisterMethods(browser)
    main_page.get_main_page()
    main_page.click_on_registration_link()
    main_page.enter_firstname(TestData.first_name_positive1)
    main_page.enter_lastname(TestData.last_name_positive1)
    main_page.enter_adress(adress)
    main_page.enter_password(TestData.password_1)
    main_page.enter_conf_passw(TestData.password_1)
    main_page.click_on_registration_btn()

    # Проверка наличия подсказки о том, что должен ввести пользователь в поле
    assert main_page.get_error_adress_text()==ErrorMessage.error_adress_message


@pytest.mark.parametrize("password", TestData.lst_invalid_passw, ids=TestData.ids_invalid_passw)
def test_negative_registration_password_boundary_values(browser, password):
    '''Тест 12. Невозможность регистрации с невалидным паролем. КЭ и ГЗ'''
    # Присвоение переменным значений текста ошибки и пароля путем параметризации
    (error_message, passw) = password

    # Заполнение анкеты регистрации
    main_page = RegisterMethods(browser)
    main_page.get_main_page()
    main_page.click_on_registration_link()
    main_page.enter_firstname(TestData.first_name_positive1)
    main_page.enter_lastname(TestData.last_name_positive1)
    main_page.enter_adress(TestData.no_register_email)
    main_page.enter_password(passw)
    main_page.enter_conf_passw(passw)
    main_page.click_on_registration_btn()

    # Проверка наличия подсказки о том, что должен ввести пользователь в поле
    assert main_page.get_error_passw_text()==error_message



def test_negative_registration_passwords_not_equal(browser):
    '''Тест 13. Невозможность регистрации при несовпадении пароля и подтверждения пароля'''

    # Заполнение анкеты регистрации
    main_page = RegisterMethods(browser)
    main_page.get_main_page()
    main_page.click_on_registration_link()
    main_page.enter_firstname(TestData.first_name_positive1)
    main_page.enter_lastname(TestData.last_name_positive1)
    main_page.enter_adress(TestData.no_register_email)
    main_page.enter_password(TestData.password_1)
    main_page.enter_conf_passw(TestData.password_2)
    main_page.click_on_registration_btn()

    # Проверка наличия подсказки о том, что введенные пароли не совпадают
    assert main_page.get_error_conf_passw_text()==ErrorMessage.error_passwords_not_equal

