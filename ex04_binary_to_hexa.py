def binary_to_hexa(binary):
    hexa = hex(int(binary, 2))
    hexa2 = str(hexa)
    return print(hexa2[2:])

try:
    binary = str(input("put your binary code for traduce it in hexa"))
    binary_to_hexa(binary)
except:
    print("Reload the script and put the binary code!")

# Correction fix
#   00010010001101000101 will be 12345
#   10101011110011011110 will be ABCDE