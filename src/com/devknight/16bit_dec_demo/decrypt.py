import sys
import os

def getKeys(keyFileName, numberKeys = 8):
    keys = read(keyFileName)

    if(len(keys)>8):
        print("[WARNING] Found more than " + numberKeys + " keys.")
        print("[NOTICE] Only using " + numberKeys + " keys.")

    return keys[:numberKeys]

def decrypt(key, inString):
    outString = bytearray()
    print("hi")
    return outString

def read(file):
    f = open(file, "rb")
    retStr = f.read()
    f.close()
    return retStr

def write(file, string):
    f = open(file, "wb")
    f.write(string)
    f.close()


THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
keyFile = os.path.join(THIS_FOLDER, sys.argv[1])
inFile = os.path.join(THIS_FOLDER, sys.argv[2])
keys = getKeys(keyFile)
string = read(inFile)
write(inFile+"-E", string)
for i in range(len(keys)-1, -1, -1):
    string = decrypt(keys[i], string)
write(inFile+"-E", string)