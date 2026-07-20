import json
import pickle
from enum import Enum
from pathlib import Path

class FileType(Enum):
    JSON = 'JSON'
    BYTE = 'BYTE'



class SerializeManager:
    '''
    My own serialize manager for serialize data with set name and type.
    Save two files with different types(JSON and BYTE).
    Uses to json and pickle for dump data.

    Attributes:
        filename (str): The name of the output file.
        filetype (FileType): The format type from the FileType Enum (JSON or BYTE).

    Also use enum for list of types and 
    pathlib for setting path where files will be save.
    '''
    def __init__(self, filename, filetype):
        '''
        init some attributes
        '''
        self.filename = filename
        self.filetype = filetype


    @staticmethod
    def path_to_folder(filename:str) -> Path:
        '''
        Function which build a path for the output files
        '''
        path = Path(r'./sprint-06/task-01_files/') / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        return path


    def serialize(self, object) -> None:
        '''
        Serialize method which has two option for saving data
        '''

        full_path = self.path_to_folder(self.filename)

        if self.filetype == FileType.BYTE:
            with open(full_path, 'wb') as file:
                pickle.dump(object, file)
        
        elif self.filetype == FileType.JSON:
            with open(full_path, 'w') as file:
                json.dump(object, file)


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc, tb):
        pass



def serialize(object, filename:str, filetype:FileType) -> None:
    '''
    Function which create an instance with attributes (filename, filetype) by using context manager (with)
    and serialized data by calling special method serialize an object.

    This script shows us how context manager works.
    At first we get an instance. After that we serialize our object. And the files with SerializeManager were closed. 
    '''
    with SerializeManager(filename, filetype) as manager:
        manager.serialize(object)



user_dict = { 'name': 'Roman', 'id': 8}

serialize(user_dict, "2", FileType.BYTE) #-> creates file with name "2" and this file will contain user_dict as byte array
serialize("String", "string.json", FileType.JSON) #-> creates file with name "string.json" and text "String"
