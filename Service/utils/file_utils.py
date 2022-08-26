from mimetypes import MimeTypes
from Service.reader import FileType


def get_file_type(file_path) -> FileType:
        ext = MimeTypes.guess_type(file_path)
        if ext[0] == "application/pdf":
            print('I found PDF!!:')
            file_type = FileType.PDF
        elif ext[0] == "text/csv":
            print('I found CSV!!:')
            file_type = FileType.CSV
        elif ext[0] == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            print('I found DOCX!!:')
            file_type = FileType.DOCX
        elif ext[0] == "text/plain" or "application/vnd.oasis.opendocument.text":
            print('I found TXT!!:')
            file_type = FileType.TXT
        else:
            file_type = FileType.UNKNOW
        return file_type
