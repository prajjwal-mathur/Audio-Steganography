import wave
from decode import decoder
from encode import encoder

keepOn = True
passwd = ""

while (keepOn):
    print("\nSelect an option: \n1) Encode\n2) Decode\n3) Exit")
    val = int(input("\nChoice: "))
    if val == 1:
        encoder()
        passwd = input("Please enter password for maximum security: ")
        print("\n================================Encoding Finished=========================================")
    elif val == 2:
        testPasswd = input("\nEnter password to decrypt: ")
        print("Password: " + passwd)
        if testPasswd == passwd:
            decoder()
        else:
            print("Incorrect password, no decryption beyond this point!!!")

    elif val == 3:
        print("Thanks for using this Audio Steganography tool")
        keepOn = False
    else:
        print("\nEnter a valid choice!")
