import mimetypes
from Parsers.typecsv import CsvReader
from Parsers.pdf import PdfReader
from Parsers.txt import TxtReader
from Parsers.typedocx import DocxReader

class Reader:
    def readFile(self, file):
        ext = mimetypes.guess_type(file)
        if ext[0] == "application/pdf":
            print('I found PDF!!:')
            reader = PdfReader()
        elif ext[0] == "text/csv":
            print('I found CSV!!:')
            reader = CsvReader()
        elif ext[0] == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            print('I found DOCX!!:')
            reader = DocxReader()
        elif ext[0] == "text/plain" or "application/vnd.oasis.opendocument.text":
            print('I found TXT!!:')
            reader = TxtReader()
        return reader

