import mimetypes
from CSV import CSVReader
from PDF import PDFReader
from TXT import TXTReader
from DOCX import DOCXReader

file = input("Please, provide full path to the file:")
ext = mimetypes.guess_type(file)

if ext[0] == "application/pdf":
    reader = PDFReader()
elif ext[0] == "text/csv":
    reader = CSVReader()
elif ext[0] == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
    reader = DOCXReader()
elif ext[0] == "text/plain" or "application/vnd.oasis.opendocument.text":
    reader = TXTReader()

file = reader.load_data_source(file)