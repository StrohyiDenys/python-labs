def show(d):
    for key, elem in d.items():
        print(key, ":", elem)
def add(d):
        while True:
            key = input("Введіть ключ: ")
            if key in d:
                print("Помилка. Даний ключ вже задано")
            else: break    
        value = {}
        value["surname"] = input("Введіть прізвище: ")
        value["name"] = input("Введіть ім'я: ")
        value["height"] = input("Введіть зріст: ")
        value["gender"] = input("Введіть стать (male/female): ")
        d[key] = value
        print("Успішно.")
def delete(d):
    try:
        key = input("Введіть ключ запису, який хочете видалити: ")
        del d[key]
        print("Успішно.")
    except KeyError:
        print("Помилка. Даного ключа немає в словнику")
def sort_by_keys(d):
    for key in sorted(d):
        print(f'{key}: {d[key]}')
def avg_male_height(d):
    height_sum = 0
    counter = 0
    for person in d.values():
        if person.get("gender") == "male":
            try:
                height_sum += int(person.get("height", 0))
                counter += 1
            except ValueError:
                print(f"Некоректний зріст для {person.get('name')}")
    if counter > 0:
        print("Середній зріст чоловіків: ", height_sum / counter)
    else:
        print("Чоловікb відсутні у словнику.")
people = {
    "0": {"surname": "Коваленко", "name": "Олександр", "height": 182, "gender": "male"},
    "1": {"surname": "Шевченко", "name": "Марія", "height": 168, "gender": "female"},
    "2": {"surname": "Бойко", "name": "Іван", "height": 176, "gender": "male"},
    "3": {"surname": "Мельник", "name": "Олена", "height": 165, "gender": "female"},
    "4": {"surname": "Бонапарт", "name": "Наполеон І", "height": 169, "gender": "male", "countries_captured": 13},
    "5": {"surname": "Сидоренко", "name": "Наталія", "height": 170, "gender": "female"},
    "6": {"surname": "Кравчук", "name": "Андрій", "height": 178, "gender": "male"},
    "7": {"surname": "Лисенко", "name": "Софія", "height": 160, "gender": "female"},
    "8": {"surname": "Гриценко", "name": "Павло", "height": 185, "gender": "male"},
    "9": {"surname": "Романюк", "name": "Катерина", "height": 167, "gender": "female"}
}
print("""
-- МЕНЮ РОБОТИ ЗІ СЛОВНИКОМ --

Якщо ви бажаєте виведення усіх значень словника, тоді натисніть -> 1 <-
Якщо ви бажаєте додати новий запис до словника, тоді натисніть -> 2 <-
Якщо ви бажаєте видалення запису зі словника, тоді натисніть -> 3 <-
Якщо ви бажаєте перегляд вмісту словника за відсортованими ключами,
тоді натисніть -> 4 <-
Якщо ви бажаєте визначити середній зріст чоловіків, тоді натисніть -> 5 <-
Якщо ви бажаєте вийти з програми, тоді натисніть -> 0 <-

----------------------------
""")
while True:
    user_input = input("Введіть пункт меню: ")
    match user_input:
        case "1":
            show(people)
        case "2":
            add(people)
        case "3":
            delete(people)
        case "4":
            sort_by_keys(people)
        case "5":
            avg_male_height(people)
        case "0":
            exit()
