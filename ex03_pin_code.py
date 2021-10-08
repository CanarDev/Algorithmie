import hashlib
attempts = 0
def test(attempts):
    for i in range(10000000, 99999999):
        codeSearch = str(i)
        resultCodeSearch = hashlib.md5(codeSearch.encode())
        ResultDigested = resultCodeSearch.hexdigest()
        FinishedResult = str(ResultDigested)
        attempts += 1
        if FinishedResult == "8a069869956a4e0cf7ac69f9c20e0d49":
            return print(f"The code is : {codeSearch} and {attempts} attempts")

test(attempts)

#password = 8a069869956a4e0cf7ac69f9c20e0d49

