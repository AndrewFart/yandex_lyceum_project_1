def decode_from_morse(code):
    if not set(code.split()).issubset(set(MorseUnCode.keys())):
        return False
    return''.join([MorseUnCode[elem] for elem in code.split()])