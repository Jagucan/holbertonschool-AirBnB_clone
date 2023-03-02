import uuid
import datetime

class BaseModel:
    """ Base Class """

    def __init__(self, *args, **kwargs):
        """ Initialize instance """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ Print str format... """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute with the current datetime """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = type(self).__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
