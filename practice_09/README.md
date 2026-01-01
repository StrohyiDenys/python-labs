# 🧮 Practice Work №9  
**Student:** Strohyi Denys, Group КНз-42-5с  
**Variant:** 13  

---

## 🇬🇧 Topic  
**Working with CSV and JSON Data**

### Objective  
To master data processing techniques for CSV and JSON formats using Python's built-in libraries.

### Tasks  
1. **CSV Processing:**
   - Parse a CSV file containing World Bank inflation data.
   - Implement error handling for file opening using `try-except`.
   - Extract and compare "Inflation, consumer prices (annual %)" for Ukraine and the USA (2010–2019).
   - Save the comparison results (difference and status) into a new CSV file.
2. **JSON Operations:**
   - Create a JSON file to store personal records (Surname, Name, Height, Gender).
   - Implement an interactive menu for:
     - Displaying JSON content.
     - Adding or deleting records.
     - Searching records by a specific field.
   - Calculate the average height of men and save the result to a separate JSON file.

---

## 🇺🇦 Тема  
**Робота з даними формату CSV та JSON**

### Мета  
Опанувати методи обробки даних у форматах CSV та JSON за допомогою вбудованих бібліотек Python.

### Завдання  
1. **Обробка CSV:**
   - Написати програму для аналізу .csv файлу з даними про інфляцію.
   - Реалізувати обробку помилок за допомогою конструкції `try-except`.
   - Знайти та порівняти показники інфляції для України та США за 2010–2019 роки.
   - Записати результати порівняння у новий .csv файл.
2. **Робота з JSON:**
   - Створити JSON-об'єкт для зберігання даних про осіб (Прізвище, Ім'я, Зріст, Стать).
   - Реалізувати інтерактивне меню:
     - Виведення вмісту JSON файлу.
     - Додавання та видалення записів.
     - Пошук даних за одним із полів.
   - Визначити середній зріст чоловіків та зберегти результат в окремий JSON файл.

---

## 🧩 Files
```text
practice_09/
├── task_1_csv/
│   ├── csv.py                                       # CSV data processing script
│   ├── API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_2479.csv    # Source inflation data
│   └── comparison.csv                               # Generated comparison results
└── task_2_json/
    ├── json.py                                      # JSON CRUD operations and menu script
    ├── people.json                                  # Main JSON data storage
    └── result.json                                  # Calculation results (average height)
