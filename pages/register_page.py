from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterLocators(BasePage):
    LOCATOR_REGISTRATION_LINK = (By.ID, 'kc-register')
    LOCATOR_SLOGAN_AUTH = (By.CSS_SELECTOR, '.rt-logo.main-header__logo')
    LOCATOR_FIRSTNAME_INPUT = (By.XPATH, '//input[@name="firstName"]')
    LOCATOR_LASTNAME_INPUT = (By.XPATH, '//input[@name="lastName"]')
    LOCATOR_REGION_TEXT = (By.CSS_SELECTOR, '.register-form__dropdown input')
    LOCATOR_ADRESS_INPUT = (By.ID, 'address')
    LOCATOR_PASSWORD_INPUT = (By.ID, 'password')
    LOCATOR_CONFIRM_PASS_INPUT = (By.ID, 'password-confirm')
    LOCATOR_REGISTER_BTN = (By.CLASS_NAME, 'register-form__reg-btn')
    LOCATOR_CONFIRM_CODE_INPUT = (By.ID, 'rt-code-0')
    LOCATOR_TITLE_REG = (By.XPATH, '//*[@id="page-right"]//h1')
    LOCATOR_PERS_ACCOUNT_BTN = (By.ID, 'lk-btn')
    LOCATOR_THIS_USERNAME_EXISTS = (By.CLASS_NAME, 'card-modal__title')
    LOCATOR_ERROR_FIRSTNAME = (By.XPATH, '//form/div[1]/div[1]/span')
    LOCATOR_ERROR_LASTNAME = (By.XPATH, '//form/div[1]/div[2]/span')
    LOCATOR_ERROR_ADRESS = (By.XPATH, '//form/div[3]/span')
    LOCATOR_ERROR_PASSWORD = (By.XPATH, '//form/div[4]/div[1]/span')
    LOCATOR_ERROR_CONF_PASSWORD = (By.XPATH, '//form/div[4]/div[2]/span')
    LOCATOR_LOGOUT_BTN = (By.ID, 'logout-btn')


class RegisterMethods(BasePage):

    def enter_firstname(self, firstname):
        firstname_field = self.find_element(RegisterLocators.LOCATOR_FIRSTNAME_INPUT)
        firstname_field.click()
        firstname_field.send_keys(firstname)
        return firstname_field

    def enter_lastname(self, lastname):
        lastname_field = self.find_element(RegisterLocators.LOCATOR_LASTNAME_INPUT)
        lastname_field.click()
        lastname_field.send_keys(lastname)
        return lastname_field

    def enter_password(self, password):
        password_field = self.find_element(RegisterLocators.LOCATOR_PASSWORD_INPUT)
        password_field.click()
        password_field.send_keys(password)
        return password_field

    def enter_conf_passw(self, password):
        conf_passw_field = self.find_element(RegisterLocators.LOCATOR_CONFIRM_PASS_INPUT)
        conf_passw_field.click()
        conf_passw_field.send_keys(password)
        return conf_passw_field

    def get_region_text(self):
        return self.find_element(RegisterLocators.LOCATOR_REGION_TEXT).text

    def enter_adress(self, adress):
        adress_field = self.find_element(RegisterLocators.LOCATOR_ADRESS_INPUT)
        adress_field.click()
        adress_field.send_keys(adress)
        return adress_field

    def click_on_registration_link(self):
        return self.find_element(RegisterLocators.LOCATOR_REGISTRATION_LINK, time=10).click()

    def click_on_registration_btn(self):
        return self.find_element(RegisterLocators.LOCATOR_REGISTER_BTN, time=10).click()

    def click_on_logout_btn(self):
        return self.find_element(RegisterLocators.LOCATOR_LOGOUT_BTN, time=10).click()

    def rt_title_is_visible(self):
        return self.is_visible(RegisterLocators.LOCATOR_SLOGAN_AUTH)

    def firstname_input_is_visible(self):
        return self.is_visible(RegisterLocators.LOCATOR_FIRSTNAME_INPUT)

    def lastname_input_is_visible(self):
        return self.is_visible(RegisterLocators.LOCATOR_LASTNAME_INPUT)

    def region_is_visible(self):
        return self.is_visible(RegisterLocators.LOCATOR_REGION_TEXT)

    def adress_input_is_visible(self):
        return self.is_visible(RegisterLocators.LOCATOR_ADRESS_INPUT)

    def password_input_is_visible(self):
        return self.is_visible(RegisterLocators.LOCATOR_PASSWORD_INPUT)

    def conf_password_input_is_visible(self):
        return self.is_visible(RegisterLocators.LOCATOR_CONFIRM_PASS_INPUT)

    def reg_btn_is_visible(self):
        return self.is_visible(RegisterLocators.LOCATOR_REGISTER_BTN)

    def confirm_code_is_visible(self):
        return self.is_visible(RegisterLocators.LOCATOR_CONFIRM_CODE_INPUT)

    def enter_confirm_code(self, confirm_code):
        confirm_code_field = self.find_element(RegisterLocators.LOCATOR_CONFIRM_CODE_INPUT)
        confirm_code_field.click()
        confirm_code_field.send_keys(confirm_code)
        return confirm_code_field

    def get_title_text(self):
        return self.find_element(RegisterLocators.LOCATOR_TITLE_REG).text

    def pers_acc_is_visible(self):
        return self.is_visible(RegisterLocators.LOCATOR_PERS_ACCOUNT_BTN)

    def this_username_exists_is_visible(self):
        return self.is_visible(RegisterLocators.LOCATOR_THIS_USERNAME_EXISTS)

    def get_error_firstname_text(self):
        return self.find_element(RegisterLocators.LOCATOR_ERROR_FIRSTNAME).text

    def get_error_lastname_text(self):
        return self.find_element(RegisterLocators.LOCATOR_ERROR_LASTNAME).text

    def get_error_adress_text(self):
        return self.find_element(RegisterLocators.LOCATOR_ERROR_ADRESS).text

    def get_error_passw_text(self):
        return self.find_element(RegisterLocators.LOCATOR_ERROR_PASSWORD).text

    def get_error_conf_passw_text(self):
        return self.find_element(RegisterLocators.LOCATOR_ERROR_CONF_PASSWORD).text

    def fill_out_registr_form(self, firstname, lastname, adress, password):
        # Заполнение анкеты регистрации
        self.switch_to_first_window()
        self.get_main_page()
        self.click_on_registration_link()
        self.enter_firstname(firstname)
        self.enter_lastname(lastname)
        self.enter_adress(adress)
        self.enter_password(password)
        self.enter_conf_passw(password)
        self.click_on_registration_btn()


