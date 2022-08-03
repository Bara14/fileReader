import mimetypes

from Service.reader import Reader


reader = Reader()
file = reader.readFile('Files/name.pdf')
file.load_data_source('Files/name.pdf')


