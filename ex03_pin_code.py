import hashlib
attempts = 0
def test(attempts, cryptedPassword):
    for i in range(10000000, 99999999):
        codeSearch = str(i)
        resultCodeSearch = hashlib.md5(codeSearch.encode())
        ResultDigested = resultCodeSearch.hexdigest()
        FinishedResult = str(ResultDigested)
        attempts += 1
        if FinishedResult == cryptedPassword:
            return print(f"The code is : {codeSearch} and you did {attempts} attempts")

try:
    cryptedPassword = str(input("Insert the 8-digit MD5 encrypted code to decrypt it."))
    test(attempts, cryptedPassword)
except:
    print("Reload the script and put the 8-digit MD5 encrypted code! ")

#password = 8a069869956a4e0cf7ac69f9c20e0d49
#Correction fix

