import wave

def decoder():
    print("\n================================Decoding Started=========================================")
    file = input("Enter the path to file: ")
    audio = wave.open(file, mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
    message = "".join(chr(
        int("".join(map(str, extracted[i:i+8])), 2)) for i in range(0, len(extracted), 8))
    decoded = message.split("###")[0]
    print("Sucessfully decoded!\nMessage found: "+ decoded)
    audio.close()
    print("\n================================Decoding Finished=========================================")
