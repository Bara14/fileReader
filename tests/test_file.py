import os
from service.utils.file_utils import get_file_type
import pytest
from service.reader import start_parsing
from main import pathToFolder
from service.reader import FileType


def test_open_existing_file():
    for file in pathToFolder:
        file_path = os.path.join(os.environ['FILE_HOME'], file)
        file_type = get_file_type(file_path)
    assert file_type == FileType.DOCX


def test_env_variable_exists():
    testpath = os.environ['FILE_HOME']
    assert testpath == '/home/rkubi/PycharmProjects/fileReader/tests/Files/'


def test_PDF_type():
    file_type = get_file_type('tests/Files/name.pdf')
    assert file_type == FileType.PDF


def test_CSV_type():
    file_type = get_file_type('tests/Files/addresses.csv')
    assert file_type == FileType.CSV


def test_DOCX_type():
    file_type = get_file_type('tests/Files/dok1.docx')
    assert file_type == FileType.DOCX


def test_TXT_type():
    file_type = get_file_type('tests/Files/sdsds.txt')
    assert file_type == FileType.TXT

def test_return_context():
    start_parsing(FileType.TXT, '/home/rkubi/PycharmProjects/fileReader/tests/Files/sdsds.txt')
    assert start_parsing == 'asdf'


