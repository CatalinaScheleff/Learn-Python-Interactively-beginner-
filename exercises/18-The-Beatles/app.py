# Your code here!!
def sing():
    lyrics = ""
    for i in range (0,11):
        if (i == 4):
            lyrics += "whisper words of wisdom, "
        elif (i == 10):
            lyrics += "there will be an answer, let it be"
        else:
            lyrics += "let it be, "
    return lyrics

print(sing())