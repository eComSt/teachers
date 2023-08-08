my_list = [1,2,34,"Hello",True,3.1]
my_var = my_list[-1]
s = "foobar"
# s[0] = "z"
my_list = list(s)
my_list[0] = "z" 

l = 0
for i in my_list:
    l+=1
# print(l)
# print(len(my_list))
my_list.insert(4,'Hello')
my_list.append(42)
my_list.remove('Hello')
del my_list[0]
if 42 in my_list:
    print("Yep")
# print(my_list)
fruit = ['apple', 'banana', 'orange']
vegetable = ['carrot', 'tomato', 'potato']
fruit.extend(vegetable)
vitamins = fruit + vegetable
a = [i for i in range(50) if i % 2 == 1 and i!=5]
b = []
for i in range(50):
    if i % 2 == 1 and i!=5:
        b.append(i)

for i, j in enumerate(a):
    print(i,j)

for i in range(len(fruit)):
    print(fruit[i],fruit[i+1])