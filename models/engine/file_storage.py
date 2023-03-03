#!/usr/bin/python3
""" File Storage Module """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ Class File Storage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        dictionary = FileStorage.__objects
        return dictionary

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                json_dict = json.load(f)
                for obj_dict in json_dict.values():
                    clase = obj_dict['__class__']
                    self.new(eval('{}({})'.format(clase, '**obj_dict')))
        except FileNotFoundError:
            pass
