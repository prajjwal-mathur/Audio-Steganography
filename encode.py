import wave
import tkinter as tk
from tkinter import filedialog

# To show only the dialog without any other GUI elements, we use withdraw method
root = tk.Tk()
root.withdraw()



def encoder():
    print("\n================================Encoding Started=========================================")

    # filedailog module opens the dialog box requiring path of file, to be put as path through askopenfilename function
    path = filedialog.askopenfilename()
    audio = wave.open(path, mode="rb")
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    message = input("Enter the message: ")
    print(message)
    message = message + int((len(frame_bytes)-(len(message)*8*8))/8) * '#'
    bits = list(
        map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in message])))
    for i, bit in enumerate(bits):
        frame_bytes[i] = (frame_bytes[i] & 254) | bit
    frame_modified = bytes(frame_bytes)
    for i in range(0, 10):
        print(frame_bytes[i])
    encodedFileName = input("Enter the file name: ")
    if encodedFileName == "":
        encodedFileName = "encoded"
    newAudio = wave.open(f'{encodedFileName}.wav', 'wb')
    newAudio.setparams(audio.getparams())
    newAudio.writeframes(frame_modified)

    newAudio.close()
    audio.close()
    print(f" |---->succesfully encoded inside {encodedFileName}.wav")
    