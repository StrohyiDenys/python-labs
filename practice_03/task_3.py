text = input("Введіть текст: ")
words = text.split()
result = []
for i in range(len(words)):
    frequency = 0;
    for j in range(len(words)):
        if words[i].lower() == words[j].lower():
            frequency += 1
    if frequency == 1:
        result.append(words[i])
print(" ".join(result))        
