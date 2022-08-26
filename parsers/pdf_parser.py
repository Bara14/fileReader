import pdfplumber
from parsers.base_parser import BaseParser

class PdfReader(BaseParser):

    def load_data_source(self, file_type, file_path) -> None:
        if self._check_file_extension(file_type):
            with pdfplumber.open(file_path) as temp:
                first_page = temp.pages[0]
                return first_page.extract_text()
        return None

    def _check_file_extension(self, file_type):
        if file_type.value > 0:
            return True
        return False