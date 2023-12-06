#!/usr/bin/python3

"""Defines the HBnB console."""

import shlex
import cmd
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

my_classes = {"BaseModel": BaseModel, "User": User}


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, args):
        """EOF signal to exit the program."""
        print("")
        return True

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

    def do_show(self, args):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """

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
        else:
            print("** no instance found **")
            return

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        args_list = shlex.split(args)
        """args_list is a list of arguments passed to the command
                shlex is a lexical analyser for simple shell-like syntax;
                and shlex.split() splits a string into a list of tokens."""
        if len(args_list) == 0:
            print("** class name missing **")
            return
        if len(args_list) == 1:
            print("** instance id missing **")
        else:
            print("** instance id missing **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name."""

        
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
