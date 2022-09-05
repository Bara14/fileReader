from parsers.base_parser import BaseParser
from service.utils.extension import check_file_extension


class TxtReader(BaseParser):
    def load_data_source(self, file_type, file_path):
        if check_file_extension(file_type):
            if '.DS_Store' not in file_path:
                with open(file_path) as txtfile:
                    text = txtfile.read()
                    print(text)
        return None

