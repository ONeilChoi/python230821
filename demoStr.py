# demoStr.py
print(dir(str))

strA = "python is very powerful"
strB = "파이썬은 강력해"
print(len(strA))
print(len(strB))
print(strA.capitalize()) #첫 글자 대문자
print(strA.count("p")) #p의 개수
print(strA.count("p",7)) #7번째 자리부터 p의 개수
result = strA.upper() #전체 대문자
print(result)
print(strA.startswith("py")) #py로 시작하는지
print(strA.endswith("py")) #끝이 py로 끝나는지
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())
data = "<<< spam and ham >>>"
result = data.strip("<> ")
print(data)
print(result)
result2 = result.replace("spam", "spam egg")
print(result2)
lst = result2.split()
print(lst)
print(":)".join(lst))