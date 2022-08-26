from parsers.base_parser import BaseParser


class fakeReader(BaseParser):
    def load_data_source(self, file_type, file_path):
        print(f'Ommiting the file {file_path}')
