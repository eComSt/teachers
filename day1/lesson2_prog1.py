login = "Max"
password = "123"

login_input = input("Введите логин: ")
password_input = input("Введите пароль: ")
if login!=login_input and password!=password_input:
    print("Неверный логин и пароль")
elif login!=login_input:
    print("Неверный логин")
elif password!=password_input:
    print("Неверный пароль")
else:
    print("Добро пожаловать!")