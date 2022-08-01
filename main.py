import mimetypes
from csv import CsvReader
from pdf import PdfReader
from txt import TxtReader
from docx import DocxReader

file = input("Please, provide full path to the file:")
ext = mimetypes.guess_type(file)

if ext[0] == "application/pdf":
    reader = PdfReader()
elif ext[0] == "text/csv":
    reader = CsvReader()
elif ext[0] == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
    reader = DocxReader()
elif ext[0] == "text/plain" or "application/vnd.oasis.opendocument.text":
    reader = TxtReader()

file = reader.load_data_source(file)