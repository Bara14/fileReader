import csv
class CSVReader:
    def readCSV(self):
        with open('addresses.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row["Name"])

    def add(self):
        return print("xsdsdfsd")


