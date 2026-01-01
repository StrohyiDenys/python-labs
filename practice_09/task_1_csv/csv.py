import csv
import sys
try:
    with open("API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_2479.csv", encoding="utf-8") as File:
        print("--- Вміст файлу ---")
        print(File.read())
        print("--- Кінець ---")
        File.seek(0)
        for _ in range(4): # перші 4 рядки файлу це коментар, пропускаємо їх
            next(File)
        reader = csv.DictReader(File)
        header = reader.fieldnames
        for row in reader:
            if row["Country Name"] == "Ukraine":
                ukraine_row = row
            if row["Country Name"] == "United States":
                usa_row = row
except:
    print("Помилка! Не вдалося обробити файл")
    sys.exit()
difference_row = {"Country Name": "Difference (UA - US)", "Country Code": "UA-US", "Indicator Name": "diff", "Indicator Code": '-'}
comparison_row = {"Country Name": "Comparison", "Country Code": "UA-US", "Indicator Name": "comprasion", "Indicator Code": '-'}
for key in header:
    if key.isdigit() and 2010 <= int(key) <= 2019:
        val_ua = ukraine_row.get(key)
        val_usa = usa_row.get(key)
    else: continue   
    if val_ua and val_usa:
        try:
            difference = float(val_ua) - float(val_usa)
            difference_row[key] = round(difference, 2)
            comparison_row[key] = (
                "US<UA" if difference > 0
                else "US>UA" if difference < 0
                else "US=UA")
        except:
            difference_row[key] = ""
            comparison_row[key] = ""
    else:
        difference_row[key] = ""
toWriting = [ukraine_row, usa_row, difference_row, comparison_row]
with open("comparison.csv", 'w', encoding="utf-8", newline='') as outFile:
    writer = csv.DictWriter(outFile, fieldnames = header)
    writer.writeheader()
    writer.writerows(toWriting)
