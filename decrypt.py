# Author: Nicholas Baron (830278807)
# Description: This program is a 16bit decrypter with an 8 bit key. It takes 16bits divides it into
# 2 bytes, a and b. The bytes are then decrypted with the function (a,b) = (b(XOR)key,a).s

import sys
import os

debug = False


def getKeys(keyFileName, numberKeys = 8):
    keys = read(keyFileName)

    if len(keys) > numberKeys:
        print("[WARNING] Found more than " + numberKeys + " keys.")
        print("[NOTICE] Only using " + numberKeys + " keys.")

    return keys[:numberKeys]


def decrypt(key, inString):
    if debug:
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


# Main Program
if sys.argv[1] == "-d":
    debug = True
    i = 1
else:
    debug = False
    i = 0

print("--Welcome to 16bit DEC decrypter.--")

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
keyFile = os.path.join(THIS_FOLDER, sys.argv[1 + i])
inFile = os.path.join(THIS_FOLDER, sys.argv[2 + i])

keys = getKeys(keyFile)
string = read(inFile)

for i in range(len(keys)-1, -1, -1):
    string = decrypt(keys[i], string)
write(inFile+"_d", string)

print("--Decryption Done--")
