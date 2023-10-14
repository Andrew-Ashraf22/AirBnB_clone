#!/usr/bin/python3
"""make the hbnb Console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """the HBNB ci

    Attributes:
        prompt (str): The prompt
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """quit the prog"""
        return True

    def do_EOF(self, arg):
        """quit with eof(Ctrl+D)"""
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
