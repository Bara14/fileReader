import os
import pytest
from Service.reader import Reader
from main import pathToFolder


def test_open_existing_file():
    for file in pathToFolder:
        reader = Reader()
        read_object = reader.readFile(os.environ['FILE_HOME'] + file)
        read_object.load_data_source(os.environ['FILE_HOME'] + file)

def test_file_not_found():
    with pytest.raises(FileNotFoundError):
       for file in pathToFolder:
            reader = Reader()
            read_object = reader.readFile('sss'+ file)
            read_object.load_data_source('sss' + file)

def test_enviromental_variable_not_found():
    with pytest.raises(KeyError):
        for file in pathToFolder:
            reader = Reader()
            read_object = reader.readFile(os.environ['FILE_HOMEa'] + file)
            read_object.load_data_source(os.environ['FILE_HOMEa'] + file)
