def F(x):
    return 10 - F(x-1) if x>1 else 1
print(F(5))