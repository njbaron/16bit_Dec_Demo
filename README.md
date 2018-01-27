# 16bit_Dec_Demo
This program encrypts and decrypts 16-bit (8-bit key) information with a simplified XOR DEC Cryptographic Method. (ECE 456)

ECE 456 Encryption/Decryption Lab 1
By Nick Baron 830278807

You need python installed!

How to run Encryption:
    -Once encrypt.py and decrypt.py have been downloaded. Place both files into a folder along with the file that you wish to encrypt.
    -In a terminal window(in windows power-shell or equivalent) move to the directory that contains the programs.
    -Use the command "python encrypt.py {-d} [key_file] [file]" for encryption. -d is used as a debug flag, it is not required.
    -Once the command has executed a new file will be generated with the "e_" beginning.

How to run Decryption
    -Use the command "python decrypt.py {-d} [key_file] [file]" for decryption.
    -Once the command has executed a new file will be generated with the "d_" beginning.

Example Commands(Using provided example files)
    -Encrypt: "python encrypt.py -d test_keys_0 test_file_0"
    -Decrypt: "python decrypt.py -d test_keys_0 e_test_file_0"
