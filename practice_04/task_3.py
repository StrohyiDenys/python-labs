def insert_at_even():
    arr = list(map(int,input('Введіть список: ').split()))
    result = []
    for elem in arr:
        result.append('newElem')
        result.append(elem)
    print(result)
insert_at_even()
