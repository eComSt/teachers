my_list2 = list('')
my_list = [1,2,34,"Hello",my_list2,True,3.1,complex(12)]
my_var = my_list[3]
my_list[4] = "world"
print(my_list)
list_to_sort = [1,3,4,6,7,3,4,6,7,8]
for i in range(len(list_to_sort)):
    for j in range(len(list_to_sort)-1):
        if list_to_sort[j]>list_to_sort[j+1]:
            list_to_sort[j],list_to_sort[j+1] = list_to_sort[j+1],list_to_sort[j]
print(list_to_sort)