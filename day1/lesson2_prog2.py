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

if oper == "+":
    print("Сумма: ", a + b)
elif oper == "-":
    print("Разность: ", a - b)
elif oper == "*":
    print("Умножение: " ,a * b)
elif oper == "/":
    if b == 0:
        print("На ноль делить нельзя")
    else:
        print("Частное: ",a / b)
elif oper == "//":
    if b == 0:
        print("На ноль делить нельзя")
    else:
        print("Целая часть: ",a // b)
elif oper == "%":
    if b == 0:
        print("На ноль делить нельзя")
    else:
        print("Остаток от деления: ",a % b)
else:
    print("Неверная операция")


 
