login_to_acc_button = ".//button[contains(text(),'Войти в аккаунт')]"  # кнопка "Войти в аккаунт"
register_button = ".//a[contains(text(),'Зарегистрироваться')]"  # кнопка "Зарегистрироваться"
forgot_password_button = ".//a[contains(text(),'Восстановить пароль')]"  # кнопка "Зарегистрироваться"
register_name_input = ".//input[contains(@name,'name')]"  # поле Имя на странице регистрации
register_email_input = ".//label[contains(text(),'Email')]/following-sibling::*"  # поле Email на странице регистрации
register_password_input = ".//input[contains(@type,'password')]"  # поле Пароль на странице регистрации
register_finish_button = ".//button[contains(text(),'Зарегистрироваться')]"  # кнопка завершения регистрации
incorrect_password_msg = ".//p[contains(text(), 'Некорректный пароль')]"  # сообщение об ошибке "Некорректный пароль"
# при регистрации
login_button = ".//button[contains(text(), 'Войти')]"  # кнопка "Войти"
make_order_button = ".//button[contains(text(), 'Оформить заказ')]"  # кнопка "Оформить заказ"
profile_button = ".//p[contains(text(), 'Личный Кабинет')]"  # кнопка "Личный кабинет"
login_from_other_page_button = ".//a[contains(text(), 'Войти')]"  # кнопка "Войти" на страницах
# регистрации/восстановления пароля
profile_settings_msg = ".//p[contains(text(), 'В этом разделе вы можете изменить свои персональные данные')]"  #
# текст в настройках Личного кабинета
constructor_button = ".//p[contains(text(), 'Конструктор')]"  # кнопка "Конструктор"
log_out_button = ".//button[contains(text(), 'Выход')]"  # кнопка "Выход" на странице настроек ЛК
sauces_tab = ".//span[contains(text(), 'Соусы')]"  # раздел "Соусы"
fillings_tab = ".//span[contains(text(), 'Начинки')]"  # раздел "Начинки"
buns_tab = ".//span[contains(text(), 'Булки')]"  # раздел "Булки"
sauces_menu = ".//h2[contains(text(), 'Соусы')]"  # начало меню с соусами
fillings_menu = ".//h2[contains(text(), 'Начинки')]"  # начало меню с начинками
buns_menu = ".//h2[contains(text(), 'Булки')]"  # начало меню с булками
