a = input("Введите первую переменную: ")
if a.isnumeric():
    a = int(a)
else:
    print("неверный ввод")
    exit()
b = input("Введите вторую переменную: ")
if b.isnumeric():
    b = int(b)
else:
    print("неверный ввод")
    exit()

oper = input("Введите операцию: ")




 
print(type(b))
summ = a + b
diff = a - b
mul = a * b
div1 = a / b
div2 = a // b
div3 = a % b
print(f"Сумма: {summ}")
print(f"Разность: {diff}")
print(f"Умножение: {mul}")
print(f"Деление: {div1}")
print(f"Целая часть: {div2}")
print(f"Дробная часть: {div3}")
