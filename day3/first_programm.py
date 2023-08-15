# numbers = []
# for _ in range(10):
#     num = int(input())
#     numbers.append(num)
def show_info(numbers):
    print(f"Summa: {sum(numbers)}")
    print(f"Srednee arifmeticheskoe: {sum(numbers)/len(numbers):.2f}")
    print(f"Max: {max(numbers)}")
    print(f"Min: {min(numbers)}")
# numbers = [int(input()) for _ in range(10)]
numbers = [1,4,6,3,7,4,2,6,8,4,1,3,5,7,3]
show_info(numbers)

