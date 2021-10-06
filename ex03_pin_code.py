import hashlib
import datetime
attempts = 0
x = datetime.datetime.now()
def test(attempts, x):
    for i in range(10000000, 99999999):
        codeSearch = str(i)
        resultCodeSearch = hashlib.md5(codeSearch.encode())
        OK = resultCodeSearch.hexdigest()
        BOOMER = str(OK)
        attempts += 1
        if BOOMER == "8a069869956a4e0cf7ac69f9c20e0d49":
            return print(f"The code is : {codeSearch} and {attempts} attempts and {x.strftime('%S')}'s")

test(attempts, x)

#password = 8a069869956a4e0cf7ac69f9c20e0d49

