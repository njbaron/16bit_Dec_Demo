def encrypt(key, string):
    if(len(key)*8 > 8):
        print("FIXME: Key Length")
        exit(1)

    if(len(string) % 2):
        print("FIXME: String length")
        exit(1)

    retString = ""

    for x in range(0, len(string), 2):
        tempString = "00"
        tempString[0] = string[x+1]
        tempString[1] = string[x] ^ key[0]
        retString = retString + tempString

    return retString