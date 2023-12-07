#!/usr/bin/python3

"""Defines the HBnB console."""

import cmd
import sys
import json
import shlex
import models
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

my_classes = {"BaseModel": BaseModel, "User": User, "State": State,
              "City": City, "Amenity": Amenity,
              "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    classes = ["BaseModel",
               "User",
               "State",
               "City",
               "Amenity",
               "Place",
               "Review"]

    def do_quit(self, args):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, args):
        """EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothing on empty line\n"""
        pass

    def do_create(self, args):
        """ Usage: create <class>
        Create a new class instance and print its id.
        """

        args = shlex.split(args)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in my_classes:
            print("** class doesn't exist **")
            return
        if args[0] in my_classes:
            """if the args[0] is in my_classes, then the class exists"""
            new_object = eval(args[0])()
            new_object.save()
            """save() saves the changes in the JSON file"""
            print(new_object.id)
            """print the id of the object"""

    def do_show(self, args):
        """Prints the string representation of an instance, format:
        show <class name> <id>."""

        args_list = shlex.split(args)
        """args_list is a list of arguments passed to the command
              shlex is a lexical analyser for simple shell-like syntax;
                and shlex.split() splits a string into a list of tokens."""
        if not args:
            print("** class name missing **")
            return
        elif args_list[0] not in my_classes:
            print("** class doesn't exist **")
            return
        elif len(args_list) == 1:
            print("** instance id missing **")
            return
        new_object = "{}.{}".format(args_list[0], args_list[1])
        """new_object is a string that is the class name an the id"""
        if new_object not in models.storage.all().keys():
            """if the new_object is not in the dictionary,
            then the object doesn't exist"""
            print("** no instance found **")
            return
        else:
            print("[{}] ({}) {}".format(args_list[0], new_object[1],
                  models.storage.all()[new_object]))
            """print the object in format [class name] (id) object"""

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        args_list = shlex.split(args)
        """args_list is a list of arguments passed to the command
                shlex is a lexical analyser for simple shell-like syntax;
                and shlex.split() splits a string into a list of tokens."""
        if len(args_list) == 0:
            print("** class name missing **")
            return
        elif args_list[0] in my_classes:
            """if the args_list[0] is in my_classes, then the class exists"""
            if len(args_list) > 1:
                """if the lenght of args_list is greater than 1,
                then the id is passed"""
                key = args_list[0] + "." + args_list[1]
                """key = args_list[0] + "." + args_list[1]
                    key is the key to search in the dictionary"""
                if key in models.storage.all():
                    del models.storage.all()[key]
                    """del(key) removes the key from the dictionary"""
                    models.storage.save()
                    """save() saves the changes in the JSON file"""
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name."""

        new_object = models.storage.all()
        """new_object is a dictionary with all the objects"""
        list_objects = []
        """list_objects is a list with all the objects"""
        if args not in my_classes:
            """if args is not empty and args is not in my_classes,
            then the class doesn't exist"""
            print("** class doesn't exist **")
            return
        if args in self.classes:
            for key, value in new_object.items():
                """for key, value in new_object.items()
                    key is the key of the dictionary
                    value is the value of the dictionary, new_object.items is a
                    generator that returns the key-value of the dictionary"""
                if args in key:
                    """if args is in key, then the class exists"""
                    toke_key = key.split(".")
                    """toke_key is a list with the class name and the id"""
                    key_new = "[" + toke_key[0] + "]"\
                        + " (" + toke_key[1] + ")"
                    list_objects.append(key_new + " " + str(value))
                    """list_objects.append(key_new + " " + str(value))
                        list_objects is a list with the objects in format
                        [class name] (id) object"""
                    print(list_objects)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)."""

        if args == '':
            print("** class name missing **")
            return
        args_list = args.split()
        if args_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args_list) == 1:
            print("** instance id missing **")
            return
        key = args_list[0] + "." + args_list[1]
        all_objects = models.storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        if len(args_list) == 2:
            print("** attribute name missing **")
            return
        if len(args_list) == 3:
            print("** value missing **")
            return
        attribute = args_list[2]
        value = args_list[3]
        if '"' in value:
            value = value.strip('"')
        """args_list[0] is the class name, args_list[1] is the id, args_list[2]
        is the attribute name, args_list[3] is the value to update"""
        try:
            setattr(all_objects[key], attribute, value)
            models.storage.save()
        except AttributeError:
            print("** attribute name missing **")
            return

if __name__ == "__main__":
    HBNBCommand().cmdloop()
