def find_duplicates():
    a = input("Введіть текст: ")
    counter = {}
    for letter in a:
        if letter.isalpha():
            counter[letter] = counter[letter]+1 if letter in counter else 1
    result = set()
    for key, value in counter.items():
        if value > 1:
            result.add(key)
    print(result)
find_duplicates()    
