#!/usr/bin/python3
""" File Storage Module """
import json
import os.path


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
            if os.path.exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        module_name = class_name.lower()
                        module = __import__('models.' + module_name, fromlist=[class_name])
                        class_ = getattr(module, class_name)
                        obj = class_(**value)
                        FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
