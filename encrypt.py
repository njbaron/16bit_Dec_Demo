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
    This functions retrieves keys from a file.
    :param keyFileName: This is the filename that is supposed to contain the keys.
    :param numberKeys: This is the number of keys that are being requested for encryption.
    :return: This is a bytes array that contains the keys.
    """
    keys = read(keyFileName)

    if len(keys) > numberKeys:
        print("[WARNING] Found more than " + numberKeys + " keys.")
        print("[NOTICE] Only using " + numberKeys + " keys.")

    return keys[:numberKeys]


def encrypt(key, inString):
    """
    This is the basic encryption function. It encrypts for only one key.
    :param key: This is the 8-bit key.
    :param inString: This is the bytes array that is to be encrypted.
    :return: This is the encrypted bytes array.
    """
    if debug:
        print("[LOG} Encrypt with key: " + chr(key))
    outString = bytearray()
    inString = bytearray(inString)

    if len(inString) % 2: # Is the string an even number of bytes? If no add a byte.
        inString.append(0x80)

    for i in range(0, len(inString)-1, 2):
        outString.append(inString[i+1])
        outString.append(inString[i] ^ key)

    return outString


def read(file):
    """
    This functions reads bytes arrays from the fiven file.
    :param file: This is the file that is to be read from.
    :return: This is the bytes array containing all the information from the file.
    """
    if debug:
        print("[LOG] Reading file: " + file)
    f = open(file, "rb") #read bytes
    retStr = f.read()
    f.close()
    return retStr


def write(file, string):
    """
    This functions writes bytes array back to a file.
    :param file: This is the file name that is to be written to.
    :param string: This is the information that is to be written to the file.
    :return: Nothing useful.
    """
    if debug:
        print("[LOG] Writing file: " + file)
    f = open(file, "wb") #write bytes
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
