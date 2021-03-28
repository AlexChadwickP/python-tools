import os
import sys
from termcolor import colored, cprint

def main():
    altColor = False
    dirs = os.listdir("./")
    for dir in dirs:
        if os.path.isfile(dir):
            cprint(dir + "  ", end='')
        else:
            cprint(dir + "", 'yellow' ,end='/  ')


main()