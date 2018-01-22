import sys



def argv_error():
    print("Error: Incorrect Command Line Args ([-e/-d],[KEYFILE],[FILE TO BE CHANGED])")
    exit(1)

print("Welcome to 16bit DEC Demo")

if(len(sys.argv) < 4):
    argv_error()

if (sys.argv[1] == "-e"):
    print("Encrypting")

elif (sys.argv[1] == "-d"):
    print("Decrypting")
else:
    argv_error()

