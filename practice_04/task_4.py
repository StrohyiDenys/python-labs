def swap_pairs():
    arr = list(map(int,input('Введіть список: ').split()))
    result = []
    for i in range(0, len(arr) - 1, 2):
        result.append(arr[i+1])
        result.append(arr[i])
    if len(arr) % 2 != 0: 
        result.append(arr[-1])
    print(result)
swap_pairs()
