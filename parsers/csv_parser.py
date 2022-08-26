import csv

from parsers.base_parser import BaseParser


class CsvReader(BaseParser):
    def load_data_source(self, file_type, file_path):
        temp = {}
        with open(file_path, newline='') as csvfile:
            temp = csv.DictReader(csvfile)
            for row in temp:
                print(row["Name"])


