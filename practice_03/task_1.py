while True:
    text = input("Введіть текст: ")
    if len(text) >= 2:
        break
    else:
        print('Помилка. Кількість символів у тексті повинна бути >= 2 ')
        
print (f"Передостанній символ рядка {text} -", text[-2])
