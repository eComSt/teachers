d = dict()
d["Том Сойер"] = "Любимая книга"
d2 = {"Книга1":"Описание книги1",}
d2["Жуль Верн"] = "Очень хороший автор"
d2.update(d)
# print(d2)
# print(d2["Книга1"])
# print(d2["Жуль Верн"])
print(d2.get("Книга2","Нет такой книги"))
print(list(d2.keys()))
print(list(d2.values()))
print(list(d2.items()))
del d2["Книга1"]
a = d2.pop("Жуль Верн")
print(a)
for i,j in d2.items():
    print(i,j)
d2.clear()
print(d2)