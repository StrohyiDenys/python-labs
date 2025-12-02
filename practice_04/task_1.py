n = int(input('Введіть N (кількість ел-тів масиву): '))
min_positive = None
for i in range(n):
    elem = float(input(f'Введіть {i} ел-т масиву: '))
    if elem > 0 and (min_positive == None or elem < min_positive):
        min_positive = elem
print(min_positive if min_positive is not None else "У масиві немає додатніх елементів")
