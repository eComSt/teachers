my_list = [1,23,4,5,6,4,2,6,7,12]
print(sum(my_list)/len(my_list))
print(my_list)
my_list.reverse()
print(my_list)
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)

my_list2 = [1,23,4,5,6,4,2,6,7,12]
sorted_list = sorted(my_list2)
print(sorted_list)
print(my_list2)
sorted_list = sorted(my_list2, reverse=True)
print(sorted_list)
print(my_list2)