words = ["Hello", "world", "Codeium"]
words2 = words[2::-1]
print(words2)
separator = " "

result = separator.join(words)

print(result.count("o"))
result = result.lower()
result = result.title()
print(result.title())
print(result[10:5:-1])
print('World' in result)