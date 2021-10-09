def binary_to_hexa(binary):
    hexa = hex(int(binary, 2))
    hexa2 = str(hexa)
    return print(hexa2[2:])


binary = str(input("put your binary code for traduce it in hexa"))
binary_to_hexa(binary)