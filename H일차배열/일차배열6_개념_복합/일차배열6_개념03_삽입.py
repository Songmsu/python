'''
    [문제]  
        a리스트가 있을 때, 리스트 사이에 값을 추가하고 
        나머지 값들은 뒤로 밀어내는 것을 삽입이라고 한다. 
        랜덤(0,5)으로 위치를 입력받고 
        a리스트 사이의 그 위치에 값 100을 삽입해 보시오.
    [예시]
        r = 3   
        a = [10,34,56,100,8,43]
'''

import random

a = [10, 34, 56, 8, 43]

idx = random.randint(0, len(a)) # idx 0~5 랜덤 값 지정
print(idx)
print("idx =", idx)
value = 100

'''
idx = 3
value = 100

10, 34, 56, 8, 43
10, 34, 56, 8, 43, 100
10, 34, 56, 100, 8, 43
방      =   값
a[5]    =   a[4]
a[4]    =   a[3]
'''

if idx == len(a): # 만약 idx가 a배열과 길이가 같다면
    a.append(value) # a배열에 value(100)값 추가
else: # 그 이외에
    a.append(value) # a배열에 value(100)값 추가
    i = len(a) - 1 # i에 a배열길이-1 값 대입
    while i > idx: # while 반복문 idx보다 작을때까지
        a[i] = a[i - 1] # a배열의 i인덱스값에 a배열의 i-1인덱스 값을 대입
        i -= 1 # 반복할때마다 i값 -1
    a[idx] = value # a배열의 idx인덱스 값에 value(100)값 대입
print("a =", a)

