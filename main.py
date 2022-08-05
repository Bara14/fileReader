from Service.reader import Reader
import os

env_var = os.environ
os.environ['FILE_HOME'] = '/home/rkubi/PycharmProjects/fileReader/Files/'
pathToFolder = os.listdir(os.environ['FILE_HOME'])

for file in pathToFolder:
    reader = Reader()
    read_object = reader.readFile(os.environ['FILE_HOME']+file)
    read_object.load_data_source(os.environ['FILE_HOME']+file)

