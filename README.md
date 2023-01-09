Этот репозиторий — является итоговым проектом курса Тестировщик-автоматизатор на Python | SkillFactory
Проект содержит тесты для личного кабинета Ростелеком https://b2c.passport.rt.ru/

Как запустить:
1. Скопировать данный репозиторий на свой компьютер.
2. Установить зависимости командой в терминале: pip install -r requirements.txt
3. В config.py измените путь на (актуальный для вашей ОС и версии вашего браузера) chromedriver или geckodriver:
5. Запуск тестов:
    1) все тесты - команда: 
       python -m pytest -v tests
    2) тесты регистрации пользователя: 
       python -m pytest -v tests/registration_test.py
    3) тесты авторизации пользователя: 
        python -m pytest -v tests/auth_test.py 
    4) тесты восстановления пароля пользователя: 
        python -m pytest -v tests/recover_passw_test.py
    5) для отдельного запуска тестов с ручным вводом кода по sms используйте:
        python -m pytest -v sms tests
    6) для отдельного запуска тестов с ручным вводом кaпчи используйте:
        python -m pytest -v capcha tests   
       
       
       