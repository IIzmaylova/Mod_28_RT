from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import re



class EmailLocators(BasePage):
    LOCATOR_EMAIL_ADRESS = (By.XPATH, '//*[contains(@class, "gap-2")]//div[contains(text(), "@tmp-mail")]')
    LOCATOR_OPEN_LAST_EMAIL = (By.CSS_SELECTOR, 'td.text-center  svg')
    LOCATOR_OPEN_RECOVERY_EMAIL = (By.XPATH, '//td[contains(text(),"Восстановление доступа")]/following-sibling::*[1]')
    LOCATOR_CONF_CODE_MAIL = (By.XPATH, '//p[contains(text(),"Ваш код :")]')
    LOCATOR_RECOVERY_CODE_MAIL = (By.XPATH, '//p[contains(text(),"Ваш код:")]')
    LOCATOR_BACK_EMAIL_BTN = (By.CSS_SELECTOR, '.gap-8.py-8 .gap-1')


class EmailMethods(BasePage):
    def get_email(self):
        return self.find_element(EmailLocators.LOCATOR_EMAIL_ADRESS).text

    def open_last_email(self):
        return self.find_element(EmailLocators.LOCATOR_OPEN_LAST_EMAIL, time=300).click()

    def open_recovery_email(self):
        return self.find_element(EmailLocators.LOCATOR_OPEN_RECOVERY_EMAIL, time=300).click()

    def get_registration_code(self):
        message_conf_code = self.find_element(EmailLocators.LOCATOR_CONF_CODE_MAIL).text
        confirm_code = message_conf_code.split(':')[-1]
        return confirm_code

    def get_recovery_code(self):
        message_conf_code = self.find_element(EmailLocators.LOCATOR_RECOVERY_CODE_MAIL).text
        confirm_code = re.split(r'[ .]+', message_conf_code)[2]
        return confirm_code

    def click_on_back_email(self):
        return self.find_element(EmailLocators.LOCATOR_BACK_EMAIL_BTN).click()



