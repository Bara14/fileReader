from parsers.base_parser import BaseParser


class TxtReader(BaseParser):
    def load_data_source(self, file_type, file_path):
        print('%%%%%%', file_path)
        if '.DS_Store' not in file_path:
            with open(file_path) as txtfile:
                text = txtfile.read()
                print(text)

