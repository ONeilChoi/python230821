# demoRamdomOS.py

import random
print(random.random())
print(random.random())
print(random.uniform(2,5))

#겹치는 숫자가 나와도 상관없다면
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])

#유니크한 숫자만 나와야 한다면
print("--sampling--")
print(random.sample(range(20),10)) 
print(random.sample(range(20),10))

from os.path import *
from os import *

print(abspath("python.exe"))
print(basename("c:\\python310\python.exe"))

if exists("c:\\python310\python.exe"):
    print("파일크기 : {0}".format(getsize("c:\\python310\python.exe")))
else:
    print("파일 없음")

print("운영체제 이름 : {0}".format(name))
print("환경변수 : {0}".format(environ))
#system("notepad.exe")    

#파일 목록
import glob
result = glob.glob("c:\\work\\*.py")
for item in result:
    print (item)