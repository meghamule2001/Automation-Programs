
# ==================
# imports
# ==================
from sys import *
import os
import hashlib

# ===============================================
# Automation operations to calculate checksum
# ===============================================
def CalculateChecksum(path,blocksize = 1024):
    fd = open(path,'rb')
    hobj = hashlib.md5()
    # 2051
    # 1 : 1024
    buffer = fd.read(blocksize)     # buffer or encode() : used to convert file data into bytes which is acceptible by hashlib
    while(len(buffer) > 0):
        hobj.update(buffer)     # update further buffer size 2 : 1024   3 : 3   4 : 0
        buffer = fd.read(blocksize) # 2 : 1024  3 : 3   4 : 0

    fd.close()
    return hobj.hexdigest()

# ===============================================
# Function to traverse directory
# ===============================================
def DirectoryTraversal(path):
    print("Contents of directory are")
        # list,list,list

    duplicate = {}      # dictonary to hold filename and checksum

    for Folder,Subfolder,Filename in os.walk(path):
        print("Directory name is : "+Folder)
        for sub in Subfolder:   # 2 : Hello
            print("Subfolder of "+Folder+" is : "+sub)
        for file in Filename:   # 1 : a.py , b.py   3 : c.py, d.py
            print("File name is : "+file)
            actualpath = os.path.join(Folder,file)
            hash = CalculateChecksum(actualpath)

            if hash in duplicate:       # that checksum is already present
                duplicate[hash].append(actualpath)
            else:       # there is no such checksum
                duplicate[hash] = [actualpath]

    return duplicate

# =============================================
# Function to display duplicate files
# =============================================
def DisplayDuplicate(duplicate):
    output = list(filter(lambda x : len(x) > 1, duplicate.values()))
    # output = ((Hello.txt, A.py, Data.txt), ())

    # duplicate = ((Hello.txt, A.py, Data.txt), (Megha.txt), (data.txt , Demo.txt), (Hello.txt), (a.txt, b.txt, c.txt))
    #           x = 3                        x = 2                     x = 3
    # output = ((Hello.txt, A.py, Data.txt), (data.txt , Demo.txt), (a.txt, b.txt, c.txt))
    if(len(output) > 0): # 3
        print("There are duplicate files")
    else:
        print("There are no duplicate files")
        return

    print("List of duplicate files are : ")
    i = 0
    icnt = 0
    for result in output:
        # print(result)
        for path in result:
            icnt = icnt + 1
            if icnt >= 2:
                i += 1
                print("%s"%path)
                os.remove(path)
        icnt = 0

    print("Number of duplicate files deleted", i)

# ===========================
# Entry point function
# ===========================
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

    arr = {}
    arr = DirectoryTraversal(argv[1])

    DisplayDuplicate(arr)

# ============================
# Starter
# ============================
if __name__=="__main__":
    main()