import docx
from parsers.base_parser import BaseParser


class DocxReader(BaseParser):
    def load_data_source(self, file_type, file_path):
        doc = docx.Document(file_path)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        print(fullText)
