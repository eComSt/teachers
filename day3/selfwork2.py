# file = open('file.txt','w', encoding="utf-8")
# for i in range(1,21):
#     file.write(f'{i}\n')
# file.close()
file = open('file.txt','w+', encoding="utf-8")

for i in file:
    print(i)
file.close()