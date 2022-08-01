import pdfplumber
from Interface import InformalParserInterface
class PdfReader(InformalParserInterface):
  def load_data_source(self, file_name):
    with pdfplumber.open(file_name) as temp:
      first_page = temp.pages[0]
      print(first_page.extract_text())