#!/usr/bin/python3
"""A module which serves as the command intepreter"""

import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.skill import Skill
from models.resource import Resource
from models.badge import Badge
from models.progress import Progress
# from models.review import Review
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """A class of the command line"""

    prompt = '(skill)'

    def __init__(self):
        super().__init__()
        self.classes = [
            "BaseModel", "User", "Skill",
            "Resource", "Progress", "Badge"
        ]
        self.commands = {
            'all': self.do_all,
            'update': self.do_update,
            'count': self.do_count,
            'show': self.do_show,
            'destroy': self.do_destroy
        }

    def emptyline(self):
        pass

    def default(self, line):
        line = line.replace("(", " ").replace(".", " ").replace(")", "").replace("\"", "").replace(",", "")
        line = line.split()
        if line[1] in self.commands:
            if len(line) > 2:
                for a in range(2, len(line)):
                    line[0] = line[0] + " " + line[a]
            self.commands[line[1]](line[0])

    def do_EOF(self, line):
        """A function To handle the EOF action
        Args:
            line: a system default variable
        """
        return True

    def do_quit(self, arg):
        'To close the shell'
        quit()
        return True

    def do_create(self, line):
        'To create a new class of BaseModel'
        if not line:
            print("** class name missing **")
            return
        if line == "BaseModel":
            model = BaseModel()
            model.save()
            print(model.id)
        elif line == "User":
            model = User()
            model.save()
            print(model.id)
        elif line == "Skill":
            model = Skill()
            model.save()
            print(model.id)
        elif line == "Badge":
            model = Badge()
            model.save()
            print(model.id)
        elif line == "Resourse":
            model = Resource()
            model.save()
            print(model.id)
        elif line == "Progress":
            model = Progress()
            model.save()
            print(model.id)
#        elif line == "Review":
#            model = Review()
#            model.save()
#            print(model.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        'Prints the string representation of an instance based \
        on the class name and id'
        if not line:
            print('** class name missing **')
            return
        line = line.split()
        if line[0] not in self.classes:
            print('** class doesn\'t exist **')
            return
        if len(line) != 2:
            print("** instance id missing **")
            return
        my_dict = storage.all()
        for key in my_dict.keys():
            a = key.split('.')
            if line[1] == a[1]:
                print(my_dict[key])
                return
            continue
        print("** no instance found **")

    def do_destroy(self, line):
        if not line:
            print('** class name missing **')
            return
        line = line.split()
        if line[0] not in self.classes:
            print('** class doesn\'t exist **')
            return
        if len(line) != 2:
            print("** instance id missing **")
            return
        my_dict = {}
        with open("file.json", mode='r', encoding='utf-8') as a:
            my_dict = json.loads(a.read())
        for key in my_dict.keys():
            a = key.split('.')
            if a[1] == line[1]:
                del (my_dict[key])
                with open("file.json", mode='w', encoding='utf-8') as a:
                    a.write(json.dumps(my_dict))
                storage.reload()
                return
            continue
        print("** no instance found **")

    def do_all(self, line):
        my_dict = storage.all()
        my_list = []
        if not line:
            for key in my_dict.keys():
                my_list.append(str(my_dict[key]))
            print(my_list)
            return
        if line not in self.classes:
            print("** class doesn't exist **")
        else:
            for key in my_dict.keys():
                a = key.split('.')
                if a[0] == line:
                    my_list.append(str(my_dict[key]))
            print(my_list)

    def do_count(self, line):
         my_dict = storage.all()
         if not line:
             print(len(my_dict))
         else:
             b = 0
             for key in my_dict.keys():
                 a = key.split('.')
                 if a[0] == line:
                     b += 1
             print(b)

    def do_update(self, line):
        if not line:
            print("** class name missing **")
            return
        line = line.split()
        if line[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(line) < 2:
            print("** instance id missing **")
            return
        my_dict = storage.all()
        for key in my_dict.keys():
            a = key.split('.')
            if line[1] == a[1]:
                if len(line) < 3:
                    print("** attribute name missing **")
                    return
                elif len(line) < 4:
                    print("** value missing **")
                    return
                setattr(my_dict[key], line[2], line[3])
                my_dict[key].save()
                return
        print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
