my_string = "'Hello world! '"
my_string2 = "'Hello world!'"
concat = my_string + ' ' + my_string2
# print(my_string.find('world'))
# if len(my_string)>len(my_string2):
#     a = 'Hello'
# else: 
#     a = 'World'
a = "Hello" if len(my_string)>len(my_string2) else "World"
print(a)