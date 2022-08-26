from enum import Enum
from parsers.csv_parser import CsvReader
from parsers.docx_parser import DocxReader
from parsers.fake_parser import fakeReader
from parsers.pdf_parser import PdfReader
from parsers.txt_parser import TxtReader


class FileType(Enum):
    UNKNOW = 0
    PDF = 1
    TXT = 2
    DOCX = 3
    CSV = 4


def start_parsing(file_type, file_path):
  parser = BaseReader.create(file_type)
  parser.load_data_source(file_type, file_path)


class BaseReader():
  @classmethod
  def create(cls, file_type: FileType):
    reader_class = None
    if file_type == FileType.CSV:
      reader_class = CsvReader
    elif file_type == FileType.DOCX:
      reader_class = DocxReader
    elif file_type == FileType.PDF:
      reader_class = PdfReader
    elif file_type == FileType.TXT:
      reader_class = TxtReader
    else:
      reader_class = fakeReader
    
    return reader_class()
