from service.reader import start_parsing
import os
from service.utils.file_utils import get_file_type


pathToFolder = os.listdir(os.environ['FILE_HOME'])

for file in pathToFolder:
    file_path = os.path.join(os.environ['FILE_HOME'], file)
    file_type = get_file_type(file_path)
    start_parsing(file_type, file_path)
