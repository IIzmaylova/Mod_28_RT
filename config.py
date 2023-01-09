base_url = 'https://b2c.passport.rt.ru'
email_url = 'https://tmp-mail.ru'


class ErrorMessage():
    error_email_message = 'Введите адрес, указанный при регистрации'
    error_phone_message = 'Введите номер телефона'
    error_login_message = 'Введите логин, указанный при регистрации'
    error_ls_message = 'Введите номер вашего лицевого счета'
    error_firstname_message = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    error_lastname_message = 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    error_adress_message = 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email ' \
                           'в формате example@email.ru'
    error_short_password = 'Длина пароля должна быть не менее 8 символов'
    error_long_password = 'Длина пароля должна быть не более 20 символов'
    error_passwords_not_equal = 'Пароли не совпадают'
    error_no_capital_letter_password = 'Пароль должен содержать хотя бы одну заглавную букву'
    # error_no_numb_spec_char_password = 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'
    error_conf_code_message = 'Неверный код. Повторите попытку'

class TestData():
    lst_valid_firstname = ["Александр", "Рики-Тики", "Ян", "Ева", "Даздрапермакукуцапольалексейян"]
    lst_valid_lastname = ["Ломако", "Рики-Тики", "По", "Мон", "Даздрапермакукуцапольалексейян"]
    ids_valid_name = ["cyrillic","hyphenated name","2 characters","3 characters", "30 characters"]

    lst_invalid_name = ["Anton", "Макс!", "Николай1", "汉字", "", "Ф", "КукуцапольДаздрапермаалексейкай",
                             "КукуцапольДаздрапермаалексейкайл"]
    ids_invalid_name = ['latin', 'special chars', 'numbers', 'hieroglyphs', 'empty', '1 characters',
                        '31 characters', '32 characters']

    lst_valid_passw = ['SFpassword', 'SFPASSWORD', 'SFpass12', 'SF@passw', 'SF123456', 'SF_123456', 'SFtest_passwordRT123']
    ids_valid_passw = ["only latin", "only CAPS", "valid with numb","valid with special char","len=8","len=9", "len=20"]

    lst_invalid_passw = [(ErrorMessage.error_short_password,''), (ErrorMessage.error_short_password,'1'),
                         (ErrorMessage.error_short_password,'Pass123'),
                         (ErrorMessage.error_long_password, 'SkillFactoryPass12345'),
                         (ErrorMessage.error_no_capital_letter_password, 'sf123456')]
    ids_invalid_passw = ["empty", "len=1", "len=7", "len=21", "without capital letter"]

    lst_invalid_adress = ["", "adress", "+7999***9321", "+7999汉字00000", "89990000000", "+7(999)0000000",
                             "@mail.ru", "test@", "test@@mail.ru", "test@mail"]
    ids_invalid_adress = ['empty', 'latin', 'special chars', 'hieroglyphs', 'format 8ХХХХХХХХХХ', 'format +7(ХХХ)ХХХХХХХ',
                          'format 7ХХХХХХХХХХ', 'format +7ХХХХХХХХХ', 'format +7ХХХХХХХХХХХ',
                          'format @mail.ru', 'format test@', 'format test@@mail.ru', 'format test@mail']

    valid_email = '96iiaspj2plryob@tmp-mail.ru'
    no_register_email = 'iiaspj2plryob96@tmp-mail.ru'
    no_unic_mail = '96iiaspj2plryob@tmp-mail.ru'
    # invalid_email = 'hecaris562@@cnxcoin.com'
    password_1 = 'UlceR123'
    password_2 = 'PassW2nd'
    password_3 = 'PassW3rd'
    wrong_password = 'PassW000'
    first_name_positive1 = 'Иван'
    last_name_positive1 = 'Смирнов'
    valid_phone = '+79990000000'
    no_unic_phone = '+79995699321'
    empty = ''
    wrong_conf_code = '000000'

