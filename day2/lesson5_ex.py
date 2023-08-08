list_var = []
while True:
    a = input("Enter variable: ")
    if a.isnumeric():
        if a == "0":
            break
        list_var.append(int(a))
print(list_var)
print("Среднее арифметическое:",sum(list_var)/len(list_var))
print("Максимальное значение:",max(list_var))
print("Минимальное значение:",min(list_var))
print("всего:",len(list_var))
