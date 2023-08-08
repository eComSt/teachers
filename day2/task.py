from random import randint

list1 = [randint(0,99) for i in range(1000000)]
list1 = [bool(i) for i in list1]
c = list1.count(True)
list2 = [randint(0,99) for i in range(1000000)]
list2 = [bool(i) for i in list2]
c2 = list2.count(True)
print(c,c2)
print(c/(c+c2))