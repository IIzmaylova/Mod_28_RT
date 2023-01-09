from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AuthLocators(BasePage):
    # Локаторы для страницы авторизации
    LOCATOR_TITLE_AUTH = (By.XPATH, '//*[@id="page-right"]//h1')
    LOCATOR_SLOGAN_AUTH = (By.CSS_SELECTOR, '.rt-logo.main-header__logo')
    LOCATOR_PHONE_TAB = (By.ID, 't-btn-tab-phone')
    LOCATOR_MAIL_TAB = (By.ID, 't-btn-tab-mail')
    LOCATOR_LOGIN_TAB = (By.ID, 't-btn-tab-login')
    LOCATOR_LS_TAB = (By.ID, 't-btn-tab-ls')
    LOCATOR_USERNAME_INPUT = (By.ID, 'username')
    LOCATOR_PASSWORD_INPUT = (By.ID, 'password')
    LOCATOR_RMBR_CHECKBOX = (By.CLASS_NAME, 'rt-checkbox__label')
    LOCATOR_FOGOT_PASSWORD = (By.ID, 'forgot_password')
    LOCATOR_LOGIN_BTN = (By.ID, 'kc-login')
    LOCATOR_REGISTRATION_BTN = (By.ID, 'kc-register')
    LOCATOR_ERROR_MESSAGE = (By.ID, 'form-error-message')
    LOCATOR_USER_AGR= (By.XPATH, "//*[text()[contains(., 'Пользовательским соглашением')]]")
    LOCATOR_CAPTCHA_IMAGE = (By.CLASS_NAME, 'rt-captcha__image')
    LOCATOR_CAPTCHA_INPUT = (By.ID, 'captcha')
    LOCATOR_CONF_CODE_INPUT = (By.ID, 'rt-code-0')
    LOCATOR_MASK_ADRESS = (By.CLASS_NAME, 'register-confirm-form-container__desc')
    LOCATOR_CHANGE_ADRESS = (By.CLASS_NAME, '.register-confirm-form__back-btn')
    LOCATOR_RESEND_CONF_CODE = (By.CSS_SELECTOR, 'svg.rt-base-icon')
    LOCATOR_PERS_ACCOUNT_BTN = (By.ID, 'lk-btn')
    LOCATOR_MESSAGE_EMPTY_EMAIL = (By.CLASS_NAME, 'rt-input-container__meta--error')
    LOCATOR_ONE_TIME_CODE_BTN = (By.ID, 'back_to_otp_btn')

class AuthMethods(BasePage):
    def enter_username(self, username):
        username_field = self.find_element(AuthLocators.LOCATOR_USERNAME_INPUT)
        username_field.click()
        username_field.send_keys(username)
        return username_field

    def enter_password(self, password):
        password_field = self.find_element(AuthLocators.LOCATOR_PASSWORD_INPUT)
        password_field.click()
        password_field.send_keys(password)
        return password_field

    def click_on_phone_swich(self):
        return self.find_element(AuthLocators.LOCATOR_PHONE_TAB, time=5).click()

    def click_on_email_swich(self):
        return self.find_element(AuthLocators.LOCATOR_MAIL_TAB, time=5).click()

    def click_on_login_swich(self):
        return self.find_element(AuthLocators.LOCATOR_LOGIN_TAB, time=5).click()

    def click_on_ls_swich(self):
        return self.find_element(AuthLocators.LOCATOR_LS_TAB, time=5).click()

    def click_on_auth_button(self):
        return self.find_element(AuthLocators.LOCATOR_LOGIN_BTN, time=5).click()

    def click_on_forgot_pass_link(self):
        return self.find_element(AuthLocators.LOCATOR_FOGOT_PASSWORD, time=5).click()

    def click_on_user_agreement(self):
        return self.find_element(AuthLocators.LOCATOR_USER_AGR, time=5).click()

    def click_on_reg_link(self):
        return self.find_element(AuthLocators.LOCATOR_REGISTRATION_BTN, time=5).click()

    def click_on_checkbox(self):
        return self.find_element(AuthLocators.LOCATOR_RMBR_CHECKBOX, time=10).click()

    def phone_tab_is_visible(self):
        return self.is_visible(AuthLocators.LOCATOR_PHONE_TAB)

    def rt_title_is_visible(self):
        return self.is_visible(AuthLocators.LOCATOR_SLOGAN_AUTH)

    def email_tab_is_visible(self):
        return self.is_visible(AuthLocators.LOCATOR_MAIL_TAB)

    def login_tab_is_visible(self):
        return self.is_visible(AuthLocators.LOCATOR_LOGIN_TAB)

    def ls_tab_is_visible(self):
        return self.is_visible(AuthLocators.LOCATOR_LS_TAB)

    def error_is_visible(self):
        return self.is_visible(AuthLocators.LOCATOR_ERROR_MESSAGE)

    def username_input_is_visible(self):
        return self.is_visible(AuthLocators.LOCATOR_USERNAME_INPUT)

    def passsw_input_is_visible(self):
        return self.is_visible(AuthLocators.LOCATOR_PASSWORD_INPUT)

    def forgot_pass_is_visible(self):
        return self.is_visible(AuthLocators.LOCATOR_FOGOT_PASSWORD)

    def color_of_text_fogot_pw(self):
        return self.find_element(AuthLocators.LOCATOR_FOGOT_PASSWORD).value_of_css_property("color")

    def auth_btn_is_visible(self):
        return self.is_visible(AuthLocators.LOCATOR_LOGIN_BTN)

    def reg_btn_is_visible(self):
        return self.is_visible(AuthLocators.LOCATOR_REGISTRATION_BTN)

    def pers_acc_is_visible(self):
        return self.is_visible(AuthLocators.LOCATOR_PERS_ACCOUNT_BTN)

    def captcha_is_visible(self):
        return self.is_visible(AuthLocators.LOCATOR_CAPTCHA_IMAGE)

    def error_message_login_is_visible(self):
        return self.is_visible(AuthLocators.LOCATOR_ERROR_MESSAGE)

    def error_message_empty_email_is_visible(self):
        return self.is_visible(AuthLocators.LOCATOR_MESSAGE_EMPTY_EMAIL)

    def get_error_username_text(self):
        return self.find_element(AuthLocators.LOCATOR_MESSAGE_EMPTY_EMAIL).text

    def get_title_text(self):
        return self.find_element(AuthLocators.LOCATOR_TITLE_AUTH).text

    def click_one_time_code_btn(self):
        return self.find_element(AuthLocators.LOCATOR_ONE_TIME_CODE_BTN, time=5).click()



