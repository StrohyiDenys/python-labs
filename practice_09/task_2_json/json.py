import json

def show(file_name):
    with open(file_name, "r", encoding="utf-8") as File:
        print(json.load(File))

def add(file_name):
        with open(file_name, "r+", encoding="utf-8") as File:
            data = json.load(File)
            while True:
                key = input("Введіть ключ: ")
                if key in data:
                    print("Помилка. Даний ключ вже задано")
                else: break    
            
            value = {}
            value["surname"] = input("Введіть прізвище: ")
            value["name"] = input("Введіть ім'я: ")
            value["height"] = int(input("Введіть зріст: "))
            value["gender"] = input("Введіть стать (male/female): ")

            data[key] = value

            File.seek(0)
            json.dump(data, File, ensure_ascii=False, indent=2)
            File.truncate()

        print("Успішно.")

def delete(file_name):
    with open(file_name, "r+", encoding="utf-8") as File:
        data = json.load(File)
        key = input("Введіть ключ запису, який треба видалити: ")
        
        if key in data:
            del data[key]
            File.seek(0)
            json.dump(data, File, ensure_ascii=False, indent=2)
            File.truncate()

            print("Запис видалено.")

        else:
            print("Ключ не знайдено.")

def find(file_name):
    with open(file_name, "r", encoding="utf-8") as File:
        people = json.load(File)
        
        fields = {"1": "surname", "2": "name", "3": "height", "4": "gender"}
        choice = input("""За яким з полів будете шукати?

                            surname - натисніть 1
                            name - натисніть 2
                            height - натисніть 3
                            gender - натисніть 4 """)

        if choice in fields:
            field_name = fields[choice]
            val = input("Введіть значення для пошуку: ")
            found = False
            
            for key, person in people.items():
                if str(person.get(field_name)) == val:
                    print(f"ID: {key}, Дані: {person}")
                    found = True
            if not found:
                print("Нічого не знайдено.")

        else:
            print("Неправильний вибір поля.")

def avg_male_height(file_name, result_file):
    
    with open(file_name, "r", encoding="utf-8") as File:
        data = json.load(File)
    height_sum = 0
    counter = 0

    for person in data.values():
        if person.get("gender") == "male":
            try:
                height_sum += int(person.get("height", 0))
                counter += 1

            except ValueError:
                continue

    if counter > 0:
        result_val = height_sum / counter
        result_data = {"average_male_height": result_val}

        print("Середній зріст чоловіків: ", result_val)
        
        with open(result_file, "w", encoding="utf-8") as ResFile:
            json.dump(result_data, ResFile, ensure_ascii=False, indent=2)

        print(f"Результат збережено у файл {result_file}")
    else:
        print("Чоловіки відсутні у файлі.")

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

with open("people.json", 'w', encoding="utf-8") as File:
    json.dump(people, File, ensure_ascii=False, indent=2)
print("""
-- МЕНЮ РОБОТИ З ФАЙЛОМ --

Якщо ви бажаєте виведення усіх значень файлу, натисніть -> 1 <-
Якщо ви бажаєте додати новий запис до файлу, натисніть -> 2 <-
Якщо ви бажаєте видалити запис з файлу, натисніть -> 3 <-
Якщо ви бажаєте знайти дані у файлі за одним із полів на вибір, натисніть -> 4 <-
Якщо ви бажаєте визначити середній зріст чоловіків, тоді натисніть -> 5 <-
Якщо ви бажаєте вийти з програми, тоді натисніть -> 0 <-

----------------------------
""")

while True:
    user_input = input("Введіть пункт меню: ")
    match user_input:
        case "1":
            show("people.json")
        case "2":
            add("people.json")
        case "3":
            delete("people.json")
        case "4":
            find("people.json")
        case "5":
            avg_male_height("people.json", "result.json")
        case "0":
            exit()
