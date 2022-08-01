import csv
from Interface import InformalParserInterface
class CSVReader(InformalParserInterface):
    def load_data_source(self, file_name):
        with open(file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print(row["Name"])



