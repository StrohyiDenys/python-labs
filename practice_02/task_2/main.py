from mod import sum_of_squares
while True:
    N = int(input('Введіть N'))
    if N < 1:
        print('N не може бути менше 1')
        continue
    break
print('Сума квадратів від 1 до N:', sum_of_squares(N))
