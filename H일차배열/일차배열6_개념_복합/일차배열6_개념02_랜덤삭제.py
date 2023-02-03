'''
    [문제]
        [조건1] 리스트에 랜덤숫자(1~100) 5개를 추가한다.
        [조건2] 랜덤으로 위 값 중 한 개만 삭제 후 출력하시오. 
    
    [예시]
        a = [1, 43, 22, 77 ,44]
        r = 3
        a = [1, 43, 22, 44]
'''

import random

a = []

for i in range(5): #5회반복
    num = random.randint(1, 100) # 1~100 랜덤값
    a.append(num) # num변수 a배열에 추가
print("삭제 전 a =", a)

idx = random.randint(0, len(a) - 1) # idx 0~4 랜덤값 추가
print("idx =", idx)

a.remove(a[idx]) # a배열에서 idx인덱스 값 제거
print("삭제 후 a =", a)



