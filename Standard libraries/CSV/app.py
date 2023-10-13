import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["trns_id", "pro_id", "price"])
    writer.writerow([1000, 1, 10])
    writer.writerow([2000, 2, 15])

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
