#!/usr/bin/python3
""" Command Interpreter """
import cmd
import shlex
import models
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


def parse(arg):
    return shlex.split(arg)


class HBNBCommand(cmd.Cmd):
    """ Class HBNBComand """
    prompt = '(hbnb) '
    classes = {'BaseModel', 'User', 'Place', 'State',
               'City', 'Amenity', 'Review'}

    def do_quit(self, arg):
        """ Quit and exit the program whit quit command """
        return True

    def do_EOF(self):
        """ Quit and exit the program whit EOF command """
        return True

    def emptyline(self):
        """ Doesn't execute anything """
        pass

    def help_quit(self):
        """ Prints the documentation for quit command """
        print("Quit command to exit the program")

    def help_EOF(self):
        """ Prints the documentation for EOF command """
        print("EOF command to exit the program")

    def help_help(self):
        """ Prints the documentation for help command """
        print("List commands with \"help\" or detailed with \"help + commad\"")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id """
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            items = models.storage.all()
            key = '{}.{}'.format(args[0], args[1])
            try:
                item = items[key]
                del items[key]
                models.storage.save()
                del item
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all instances """
        args = parse(arg)
        objs = models.storage.all()
        item_list = []
        if len(args) >= 1:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                for key, item in objs.items():
                    if key.startswith(args[0]):
                        item_list.append(item.__str__())
                print(item_list)
        else:
            for item in objs.values():
                item_list.append(item.__str__())
            print(item_list)

    def do_show(self, arg):
        """ Prints the string representation of an instance """
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            items = models.storage.all()
            key = '{}.{}'.format(args[0], args[1])
            try:
                item = items[key]
                print(item)
            except KeyError:
                print("** no instance found **")

    def do_create(self, arg):
        """  Creates a new instance, save it and prints the id """
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            item = eval("{}()".format(args[0]))
            print(item.id)
            models.storage.new(item)
            models.storage.save()

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """
        args = parse(arg)
        items = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = '{}.{}'.format(args[0], args[1])
            try:
                item = items[key]
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    try:
                        eval(args[3])
                    except (SyntaxError, NameError):
                        args[3] = "'{}'".format(args[3])
                    setattr(item, args[2], eval(args[3]))
                    item.save()
            except KeyError:
                print("** no instance found **")

    def cmdloop(self):
        """ Quit the program whit Ctrl + C """
        try:
            super().cmdloop()
        except KeyboardInterrupt:
            return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
