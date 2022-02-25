
from sys import *
import os
import hashlib

# Demo

def CalculateChecksum(path,blocksize = 1024):
    fd = open(path,'rb')
    hobj = hashlib.md5()

    buffer = fd.read(blocksize)     # buffer or encode() : used to convert file data into bytes which is acceptible by hashlib
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fd.read(blocksize)

    fd.close()
    return hobj.hexdigest()

def DirectoryTraversal(path):
    print("Contents of directory are")
        # list,list,list
    for Folder,Subfolder,Filename in os.walk(path):
        print("Directory name is : "+Folder)
        for sub in Subfolder:   # 2 : Hello
            print("Subfolder of "+Folder+" is : "+sub)
        for file in Filename:   # 1 : a.py , b.py   3 : c.py, d.py
            print("File name is : "+file)
            actualpath = os.path.join(Folder,file)
            hash = CalculateChecksum(actualpath)
            print(hash)

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

    DirectoryTraversal(argv[1])

if __name__=="__main__":
    main()