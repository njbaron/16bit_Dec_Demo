"""
Author: Nicholas Baron (830278807)
Description: This program is a 16bit decrypter with an 8 bit key. It takes 16bits divides it into
2 bytes, a and b. The bytes are then decrypted with the function (a,b) = (b(XOR)key,a).s
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
        print("[WARNING] Found more than " + str(numberKeys) + " keys.")
        print("[NOTICE] Using " + str(numberKeys) + " keys.")
    elif len(keys) < numberKeys:
        print("[WARNING] Found less than " + str(numberKeys) + " keys. This is making your encryption less secure!")
        print("[NOTICE] Using " + str(len(keys)) + " keys.")
    elif len(keys) == 0:
        print("[ERROR] Key file found to be empty. Cannot continue.")
        exit(1)

    return keys[:numberKeys]


def decrypt(key, inString):
    """
    This is the method that handles decryption for specific keys.
    :param key: This is the 8-bit key that is being decrypted.
    :param inString: This is the string that is to be encrypted.
    :return: This is the decrypted string.
    """

    if len(inString) < 1:
        print("[WARNING] String give to decrypt was found to be empty.")
        return inString

    if debug:
        print("[LOG} Decrypt with key: " + chr(key))
    outString = bytearray()
    inString = bytearray(inString)

    for i in range(0, len(inString)-1, 2):
        outString.append(inString[i+1] ^ key)
        outString.append(inString[i])

    if outString[len(outString)-1] == 0x80: # Is there a buffer? If so remove it.
        outString = outString[:-1]

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
    f = open(file, "wb") # write bytes
    f.write(string)
    f.close()


"""Main Program"""
if len(sys.arv) > 3 or len(sys.argv) < 2:
    print("[ERROR] Incorrect arguments: Expecting \"python decrypt.py {-d} [key_file] [file]\"")
    exit(1)
if sys.argv[1] == "-d":
    debug = True
    i = 1
else:
    debug = False
    i = 0

print("--Welcome to 16bit DEC decrypter.--")

keyFile = os.path.join(sys.argv[1 + i])
inFile = os.path.join(sys.argv[2 + i])

keys = getKeys(keyFile)
string = read(inFile)

for i in range(len(keys)-1, -1, -1):
    string = decrypt(keys[i], string)
write("d_" + inFile, string)

print("--Decryption Done--")
