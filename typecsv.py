import csv
from Interface import InformalParserInterface


class CsvReader(InformalParserInterface):
    def load_data_source(self, file_name):
        with open(file_name, newline='') as csvfile:
            temp = csv.DictReader(csvfile)
        return temp
       #     for row in reader:
        #        print(row["Name"])

    def print_text(self, temp):
        for row in temp:
            print(row["Name"])


