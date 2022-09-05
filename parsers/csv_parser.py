import csv
from service.utils.extension import check_file_extension
from parsers.base_parser import BaseParser


class CsvReader(BaseParser):
    def load_data_source(self, file_type, file_path) -> None:
        if check_file_extension(file_type):
            temp = {}
            with open(file_path, newline='') as csvfile:
                temp = csv.DictReader(csvfile)
                for row in temp:
                    print(row["Name"])
        return None



