import csv
import json

csv_file = 'insurance.csv'
json_file = 'insurance.json'

data = []

with open(csv_file, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Convert numeric fields
        row['age'] = int(row['age'])
        row['bmi'] = float(row['bmi'])
        row['children'] = int(row['children'])
        row['charges'] = float(row['charges'])
        data.append(row)

with open(json_file, 'w') as f:
    json.dump(data, f, indent=4)

print(f"{len(data)} records converted to {json_file}")