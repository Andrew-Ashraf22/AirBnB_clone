#!/usr/bin/python3
"""make the hbnb Console"""
import cmd
import json
import datetime
import uuid
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """the HBNB ci

    Attributes:
        prompt (str): The prompt
    """

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }
    prompt = '(hbnb) '

    def emptyline(self):
        """Nothing when empyline is entered"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """quit with eof(Ctrl+D)"""
        print()
        return True

    def do_create(self, arg):
        """create a new obj"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg)().id)
            storage.save()

    def do_show(self, arg):
        """print the string reps"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            k = args[0] + '.' + args[1]
            if k in models.storage.all():
                print(models.storage.all()[k])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """delete an inst"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            k = args[0] + '.' + args[1]
            if k in models.storage.all():
                del models.storage.all()[k]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """print all insts of class"""
        if arg and arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj = []
            for k in models.storage.all():
                if not arg or k.split('.')[0] == arg:
                    obj.append(str(models.storage.all()[k]))
            print(obj)

    def do_update(self, arg):
        """update inst"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            k = args[0] + '.' + args[1]
            if k in models.storage.all():
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    name = args[2]
                    value = args[3]
                    obj = models.storage.all()[k]
                    setattr(obj, name, value)
                    obj.save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
