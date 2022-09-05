import docx
from parsers.base_parser import BaseParser
from service.utils.extension import check_file_extension


class DocxReader(BaseParser):
    def load_data_source(self, file_type, file_path):
        if check_file_extension(file_type):
            doc = docx.Document(file_path)
            fullText = []
            for para in doc.paragraphs:
                fullText.append(para.text)
            print(fullText)
        return None
