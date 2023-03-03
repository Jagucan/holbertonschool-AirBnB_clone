#!/usr/bin/python3
""" Command Interpreter """
import cmd
import shlex
import models

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit and exit the program whit quit command """
        return True

    def do_EOF(self, arg):
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
        print("List available commands with \"help\" or detailed help with \"help cmd\"")

    def do_create(self, arg):
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__class__:
            print("** class doesn't exist **")
        else:
            item = eval("{}()".format(args[0]))
            print(item.id)
            models.storage.save
    
    def parse(arg):
        return shlex.split(arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()


