"""
Author: Nicholas Baron (830278807)
Description: This program is a 16bit encrypter with an 8 bit key. It takes 16bits divides it into
2 bytes, a and b. The bytes are then encrypted with the function (a,b) = (b,a(XOR)key).
"""

import sys
import os

debug = False


def getKeys(keyFileName, numberKeys = 8):
    """

    :param keyFileName:
    :param numberKeys:
    :return:
    """
    keys = read(keyFileName)

    if len(keys) > numberKeys:
        print("[WARNING] Found more than " + numberKeys + " keys.")
        print("[NOTICE] Only using " + numberKeys + " keys.")

    return keys[:numberKeys]


def encrypt(key, inString):
    """

    :param key:
    :param inString:
    :return:
    """
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
    """

    :param file:
    :return:
    """
    if debug:
        print("[LOG] Reading file: " + file)
    f = open(file, "rb")
    retStr = f.read()
    f.close()
    return retStr


def write(file, string):
    """

    :param file:
    :param string:
    :return:
    """
    if debug:
        print("[LOG] Writing file: " + file)
    f = open(file, "wb")
    f.write(string)
    f.close()


"""Main Program"""
if sys.argv[1] == "-d":
    debug = True
    i = 1
else:
    debug = False
    i = 0

print("--Welcome to 16bit DEC encrypter.--")

keyFile = os.path.join(sys.argv[1 + i])
inFile = os.path.join(sys.argv[2 + i])

keys = getKeys(keyFile)
string = read(inFile)

for i in range(0, len(keys)):
    string = encrypt(keys[i], string)
write("e_" + inFile, string)

print("--Encryption Done--")
