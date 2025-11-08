import math

def calculate_z(x, y):
    z = math.cos(x)**2 + math.sin(y)**2
    return z
def sum_of_squares(N):
    S = 0
    for i in range(1, N + 1):
        S += i**2
    return S

## calculate_z():
x = float(input('Введіть x: '))
y = float(input('Введіть y: '))
print('Значення z: ', calculate_z(x,y))

## sum_of_squares():
N = int(input('Введіть N: '))
print('Сума квадратів від 1 до N:', sum_of_squares(N))
