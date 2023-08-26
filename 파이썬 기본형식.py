# 파이썬 기본형식.py

x = 100
y = 3.14
print( type(x) )
print( type(y) )

strA = "python is very powerful"
strB = "파이썬은 강력해"
print( type(strA ))
print( type(strB ))

strC = """ 다중 라인으로 저장할 경우
이렇게 묶으면 
다중 라인으로 인식합니다."""
print(strC)

#list
lst = [1,2,3,4,5]
print(type(lst))
print(len(lst))
print(lst)

#리스트에 입력, 수정, 삭제, 검색하기
lst.append(6) #숫자 6을 추가
lst.insert(1,0) # 1번째 인덱스에 0 추가
lst[0] = 100 # 0번째 인덱스를 100으로 교체
lst.remove(5) # 5라는 값을 제거
print(lst) # 출력

#튜플은 초기화하면 읽기전용으로 사용됨
#용도가 제한적, 여러 개의 데이터를 실어 나르는 형태
tp = (100, 200, 300)
print(len(tp))
print( tp.index(200) )
print("id : %s, name: %s" % ("Kim", "김유신"))

#함수 정의 
def times(a,b):
    return a+b, a*b 

#호출
result = times(3,4)
print(result)
print(result[0])
print(result[1])

#한번에 데이터 입력 (*은 Tuple을 의미)
args = (5,6)
print(times(*args))