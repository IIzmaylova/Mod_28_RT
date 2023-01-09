from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class RecoverPassLocators(BasePage):
    LOCATOR_FOGOT_PASSWORD = (By.ID, 'forgot_password')
    LOCATOR_PHONE_TAB = (By.ID, 't-btn-tab-phone')
    LOCATOR_MAIL_TAB = (By.ID, 't-btn-tab-mail')
    LOCATOR_LOGIN_TAB = (By.ID, 't-btn-tab-login')
    LOCATOR_LS_TAB = (By.ID, 't-btn-tab-ls')
    LOCATOR_USERNAME_INPUT = (By.ID, 'username')
    LOCATOR_CAPTCHA_INPUT = (By.ID, 'captcha')
    LOCATOR_CAPTCHA_IMG = (By.CLASS_NAME, 'rt-captcha__image')
    LOCATOR_CONTINUE_BTN = (By.ID, 'reset')
    LOCATOR_BACK_AUTH_BTN = (By.ID, 'reset-back')
    LOCATOR_CONFIRM_CODE_INPUT = (By.ID, 'rt-code-0')
    LOCATOR_NEW_PASSW_INPUT = (By.ID, 'password-new')
    LOCATOR_CONFIRM_PASSW_INPUT = (By.ID, 'password-confirm')
    LOCATOR_SAVE_PASSW_BTN = (By.ID, 't-btn-reset-pass')
    LOCATOR_TITLE_PAGE = (By.TAG_NAME, 'h1')
    LOCATOR_RESEND_CONF_CODE = (By.CLASS_NAME, 'code-input-container__resend')
    LOCATOR_ERROR_CONF_CODE = (By.ID, 'form-error-message')
    LOCATOR_INFO_RECOVERY_PASSW = (By.XPATH, '//h1[contains (text(), "Восстановление пароля")]')
    LOCATOR_SAVE_NEW_PASSW_BTN = (By.ID, 't-btn-reset-pass')
    LOCATOR_ERROR_NEW_PASSW = (By.XPATH, '//form/div/div[1]/span')

class RecoverPassMethods(BasePage):
    def click_on_forgot_pass_link(self):
        return self.find_element(RecoverPassLocators.LOCATOR_FOGOT_PASSWORD, time=5).click()

    def click_on_phone_swich(self):
        return self.find_element(RecoverPassLocators.LOCATOR_PHONE_TAB, time=5).click()

    def click_on_email_swich(self):
        return self.find_element(RecoverPassLocators.LOCATOR_MAIL_TAB, time=5).click()

    def enter_username(self, username):
        username_field = self.find_element(RecoverPassLocators.LOCATOR_USERNAME_INPUT)
        username_field.click()
        username_field.send_keys(username)
        return username_field

    def click_on_continue_button(self):
        return self.find_element(RecoverPassLocators.LOCATOR_CONTINUE_BTN, time=5).click()

    def click_on_resend_code(self):
        return self.find_element(RecoverPassLocators.LOCATOR_RESEND_CONF_CODE, time=200).click()

    def enter_confirm_code(self, confirm_code):
        confirm_code_field = self.find_element(RecoverPassLocators.LOCATOR_CONFIRM_CODE_INPUT)
        confirm_code_field.click()
        confirm_code_field.send_keys(confirm_code)
        return confirm_code_field

    def enter_new_password(self, password):
        new_password = self.find_element(RecoverPassLocators.LOCATOR_NEW_PASSW_INPUT)
        new_password.click()
        new_password.send_keys(password)
        return new_password

    def enter_confirm_password(self, password):
        confirm_password = self.find_element(RecoverPassLocators.LOCATOR_CONFIRM_PASSW_INPUT)
        confirm_password.click()
        confirm_password.send_keys(password)
        return confirm_password

    def click_on_save_passw_btn(self):
        return self.find_element(RecoverPassLocators.LOCATOR_SAVE_PASSW_BTN, time=10).click()

    def phone_tab_is_visible(self):
        return self.is_visible(RecoverPassLocators.LOCATOR_PHONE_TAB)

    def email_tab_is_visible(self):
        return self.is_visible(RecoverPassLocators.LOCATOR_MAIL_TAB)

    def login_tab_is_visible(self):
        return self.is_visible(RecoverPassLocators.LOCATOR_LOGIN_TAB)

    def ls_tab_is_visible(self):
        return self.is_visible(RecoverPassLocators.LOCATOR_LS_TAB)

    def save_passw_btn_is_visible(self):
        return self.is_visible(RecoverPassLocators.LOCATOR_SAVE_PASSW_BTN)

    def captcha_is_visible(self):
        return self.is_visible(RecoverPassLocators.LOCATOR_CAPTCHA_IMG)

    def confirm_code_is_visible(self):
        return self.is_visible(RecoverPassLocators.LOCATOR_CONFIRM_CODE_INPUT)

    def username_unput_is_visible(self):
        return self.is_visible(RecoverPassLocators.LOCATOR_USERNAME_INPUT)

    def captcha_input_is_visible(self):
        return self.is_visible(RecoverPassLocators.LOCATOR_CAPTCHA_INPUT)

    def continue_btn_is_visible(self):
        return self.is_visible(RecoverPassLocators.LOCATOR_CONTINUE_BTN)

    def back_auth_btn_is_visible(self):
        return self.is_visible(RecoverPassLocators.LOCATOR_BACK_AUTH_BTN)

    def get_title_text(self):
        return self.find_element(RecoverPassLocators.LOCATOR_TITLE_PAGE).text

    def get_error_conf_code_text(self):
        return self.find_element(RecoverPassLocators.LOCATOR_ERROR_CONF_CODE).text

    def get_error_new_passw_text(self):
        return self.find_element(RecoverPassLocators.LOCATOR_ERROR_NEW_PASSW).text



