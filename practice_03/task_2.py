import re 
text = input("Введіть текст: ")
print(re.sub('[^\W\d_]', '', text))
