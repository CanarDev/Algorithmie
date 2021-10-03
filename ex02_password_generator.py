import random
arrayPassword = []
def randomPassword(value, arrayPassword):
    for i in range(value):
        n = random.choice(list(caracterList))
        arrayPassword.append(n)
    return arrayPassword


caracterList = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J",
                "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s",
                "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
value = int(input("Hello There ! How many caracter do you want in your BADASS PASSWORD?"))
print(''.join(randomPassword(value, arrayPassword)))