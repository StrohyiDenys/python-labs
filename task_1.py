while True:
    a = int(input('Введіть значення a:'))
    b = int(input('Введіть значення b:'))
    if((1 <= a <= 100) and (1 <= b <= 100)):
        break
    else:
        print('Помилка. Числа мають знаходитися в діапазоні від 1 до 100')
if a > b:
    X = b/a+61
elif a == b:
    X = -5
else: #a < b
    X = (b-a)/b
print('X = ', X)
