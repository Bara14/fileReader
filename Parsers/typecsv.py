import csv
from Interface import InformalParserInterface


class CsvReader(InformalParserInterface):
    def load_data_source(self, file_name):
        temp = {}
        with open(file_name, newline='') as csvfile:
            temp = csv.DictReader(csvfile)
            for row in temp:
                print(row["Name"])


