import mimetypes
from service.reader import FileType
from service.utils.logger import logger


def get_file_type(file_path) -> FileType:
    logger.info('filePath: ' + file_path)
    ext = mimetypes.guess_type(file_path)
    if ext[0] == "application/pdf":
        logger.info('I found PDF!!:')
        file_type = FileType.PDF
    elif ext[0] == "text/csv":
        logger.info('I found CSV!!:')
        file_type = FileType.CSV
    elif ext[0] == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        logger.info('I found DOCX!!:')
        file_type = FileType.DOCX
    elif ext[0] == "text/plain" or "application/vnd.oasis.opendocument.text":
        logger.info('I found TXT!!:')
        file_type = FileType.TXT
    else:
        file_type = FileType.UNKNOW
    return file_type


