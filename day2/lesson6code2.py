catalog = dict()
while True:
    print('Список действий:')
    print('1 - Добавить книгу')
    print('2 - Найти книгу')
    print('3 - Удалить книгу')
    print('4 - Все книги')
    print('0 - Выход')
    choise = input('Выберите действие: ')
    if choise == '0':break
    elif choise == '1':
        title = input("Введите название книги: ")
        while title in catalog:
            title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        catalog[title]=author
    elif choise == '2':
        title = input("Введите название книги: ")
        if title in catalog:
            print("Информация о книге:")
            print("Название:",title)
            print("Автор:",catalog[title])
        else:
            print("Такой книги нет")
    elif choise == '3':
        title = input("Введите название книги: ")
        if title in catalog:
            del catalog[title]
        else:
            print("Такой книги нет")
    elif choise == '4':
        for i in catalog:
            print(f"Название:{i}, Автор:{catalog[i]}")
    else:
        print('Неверный вввод')