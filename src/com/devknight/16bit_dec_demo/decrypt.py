import sys
import os

debug = False

def getKeys(keyFileName, numberKeys = 8):
    keys = read(keyFileName)

    if(len(keys)>numberKeys):
        print("[WARNING] Found more than " + numberKeys + " keys.")
        print("[NOTICE] Only using " + numberKeys + " keys.")

    return keys[:numberKeys]

def decrypt(key, inString):
    print("[LOG} Decrypt with key: " + chr(key))
    outString = bytearray()
    inString = bytearray(inString)

    for i in range(0, len(inString)-1, 2):
        outString.append(inString[i+1] ^ key)
        outString.append(inString[i])

    if outString[len(outString)-1] == 0x10:
        outString = outString[:-1]

    return outString

def read(file):
    print("[LOG] Reading file: " + file)
    f = open(file, "rb")
    retStr = f.read()
    f.close()
    return retStr

def write(file, string):
    print("[LOG] Writing file: " + file)
    f = open(file, "wb")
    f.write(string)
    f.close()


print("--Welcome to 16bit DEC decrypter.--")
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
keyFile = os.path.join(THIS_FOLDER, sys.argv[1])
inFile = os.path.join(THIS_FOLDER, sys.argv[2])
keys = getKeys(keyFile)
string = read(inFile)
for i in range(len(keys)-1, -1, -1):
    string = decrypt(keys[i], string)
write(inFile+"_d", string)