arr = []
for i in range (0,7):
    arr.append([])
    for j in range (0,7):
        arr[i].append(1 if (i % 2 == 0) else 0)
for row in arr:
    print(' '.join(str(elem) for elem in row))
