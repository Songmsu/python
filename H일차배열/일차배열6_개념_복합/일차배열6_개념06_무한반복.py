'''
    [문제]
        [조건1] 리스트에 랜덤숫자(1~100) 5개를 추가한다.
        [조건2] 랜덤으로 홀수만 저장한다.   
'''
'''
    문제만 보면 5번 반복하면 될 것 같지만 함정이다. 
    홀수만 저장이기 때문에 무한반복을 사용해야 한다.
'''
import random

a = []

# 방법1)
count = 0
while True: #while 반복문
    r = random.randint(1, 100)
    print(r, end=" ")
    if r % 2 == 1: # 랜덤값 r이 홀수면
        a.append(r) # a배열에 추가
        count += 1 # count 1증가
    
    if count == 5: # count가 5가되면
        break # 반복 멈춤
print()
print("a =", a)

# 방법2) 0~4 즉 5번 반복아닌가?
a = []
count = 0

i = 0
while i < 5:
    r = random.randint(1, 100)
    print(r, end=" ")
    if r % 2 == 1:
        a.append(r)
        i += 1
print()
print("a =", a)