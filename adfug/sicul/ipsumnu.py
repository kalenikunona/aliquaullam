import csv
with open('example.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['John', 25, 'New York'])
