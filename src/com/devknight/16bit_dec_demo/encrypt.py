import sys
import os

debug = False
i = 0

def getKeys(keyFileName, numberKeys = 8):
    keys = read(keyFileName)

    if(len(keys)>numberKeys):
        print("[WARNING] Found more than " + numberKeys + " keys.")
        print("[NOTICE] Only using " + numberKeys + " keys.")

    return keys[:numberKeys]

def encrypt(key, inString):
    if debug:
        print("[LOG} Encrypt with key: " + chr(key))
    outString = bytearray()
    inString = bytearray(inString)

    if len(inString) % 2:
        inString.append(0x10)

    for i in range(0, len(inString)-1, 2):
        outString.append(inString[i+1])
        outString.append(inString[i] ^ key)

    return outString

def read(file):
    if debug:
        print("[LOG] Reading file: " + file)
    f = open(file, "rb")
    retStr = f.read()
    f.close()
    return retStr

def write(file, string):
    if debug:
        print("[LOG] Writing file: " + file)
    f = open(file, "wb")
    f.write(string)
    f.close()


try:
    if sys.argv[1] == "-d":
        debug = True
        i = 1
except:
    debug = False
    i = 0

if debug:
    print("--Welcome to 16bit DEC encrypter.--")
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
keyFile = os.path.join(THIS_FOLDER, sys.argv[1 + i])
inFile = os.path.join(THIS_FOLDER, sys.argv[2 + i])
keys = getKeys(keyFile)
string = read(inFile)
for i in range(0, len(keys)):
    string = encrypt(keys[i], string)
write(inFile+"_e", string)
