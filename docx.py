import docx
from Interface import InformalParserInterface

class DocxReader(InformalParserInterface):
  def load_data_source(self, file_name):
      doc = docx.Document(file_name)
      fullText = []
      for para in doc.paragraphs:
          fullText.append(para.text)
      print(fullText)