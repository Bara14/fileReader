import os
from service.utils.file_utils import get_file_type
import pytest
from service.reader import start_parsing
from main import pathToFolder
from service.reader import FileType


def test_open_existing_file():
    file = 'sdsds.pdfaaaaa'
    for file in pathToFolder:
        file_path = os.path.join(os.environ['FILE_HOME'], file)
        file_type = get_file_type(file)
    assert file_type == FileType.DOCX

# def test_file_not_found():
#     with pytest.raises(FileNotFoundError):
#        for file in pathToFolder:
#             reader = Reader()
#             read_object = reader.readFile('sss'+ file)
#             read_object.load_data_source('sss' + file)


# def test_env_variable_not_found():
#     with pytest.raises(KeyError):
#         for file in pathToFolder:
#             reader = Reader()
#             read_object = reader.readFile(os.environ['FILE_HOMEa'] + file)
#             read_object.load_data_source(os.environ['FILE_HOMEa'] + file)