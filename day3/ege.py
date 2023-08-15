
def func(n):
    return n if n<2 else func(n//2)+func(n%2)
count = 0
for i in range(2**30):
    if func(i) == 27:
        count+=1    
print(count)
