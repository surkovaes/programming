import csv
import json

with open('MOCKDATA.json') as f:
    data_dict = json.load(f)

with open('eggs.csv', 'w', newline='') as csvfile:
    jsonwriter = csv.writer(
        csvfile, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
    jsonwriter.writerow(data_dict[0].keys())
    keys = data_dict[0].keys()
    for el in data_dict:
        jsonwriter.writerow(el.values())
print("Файл записан")
