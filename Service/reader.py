import mimetypes
from typecsv import CsvReader
from pdf import PdfReader
from txt import TxtReader
from docx import DocxReader

class Reader:
    def readFile(self, file):
        ext = mimetypes.guess_type(file)
        if ext[0] == "application/pdf":
            reader = PdfReader()
        elif ext[0] == "text/csv":
            reader = CsvReader()
        elif ext[0] == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            reader = DocxReader()
        elif ext[0] == "text/plain" or "application/vnd.oasis.opendocument.text":
            reader = TxtReader()
        return reader

