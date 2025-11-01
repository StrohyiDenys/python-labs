while True:
    n = int(input('Введіть N'))
    if 1 < n < 9:
        break;
    else:
        print('Помилка. Введене число повинно задовольняти умові 1<N<9');
for i in range(1, n+1):
    row = ' ' * (n - i)
    for j in range(1, i+1):
        row += str(j)
    print(row)    
