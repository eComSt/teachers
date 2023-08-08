s1 = "Hello"
s2 = "'world'"
s3 = "!"
num = 123
hi = s1 + " " + s2 + " " + s3 + " " + str(num)
hello = f"{s1},{s2},{s3},{num}"
list_hello = hello.split(",")
for i in list_hello:
    print(f"{i};{i.isnumeric()}")
print(list_hello)
# for i in range(10):
#     print(f'i={i}')