
from sys import *
import os

def main():
    print("Marvellous Infosystems")
    print("Directory traversal script")

    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1] == "-h" or (argv[1] == "-H")):
        print("It is Directory cleaner script")
        exit()

    if((argv[1] == "-u") or (argv[1] == "U")):
        print("Usage : Provide the absolute path of the target directory")
        exit()

if __name__=="__main__":
    main()