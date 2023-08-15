def sum_digits(num):
    summ = 0
    while num>0:
        summ += num%10
        num //= 10
    return summ
    print("AFTER RETURN")

def sum_digits2(num):
    return sum([int(i) for i in str(num)])

sum_digits3 = lambda num:sum([int(i) for i in str(num)])

num = int(input())
summa = sum_digits3(num)
print(summa)