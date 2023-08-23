#정규표현식(특정한 패턴)
import re

#원본 로그파일
f = open('c:\\work\\PV3.txt', 'rt')
#복사본 로그파일
g = open('c:\\work\\PV3_copy.txt','wt',encoding = 'utf-8')

#많은 라인의 파일이면 한 번에 한 줄식 읽어서 처리
#파일의 EOF(End Of File)이 아니면 계속 읽도록 함

line = f.readline()
while(line != ''):
    if(re.search("\d{4}}", line)):
        g.write(line + "\n")
    line = f.readline()

f.close()
g.close()