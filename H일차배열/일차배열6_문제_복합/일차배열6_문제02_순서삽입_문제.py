'''
    [문제]  
        아래 a리스트는 순서대로 값이 저장되어있다.
        랜덤(1~70)숫자 하나를 저장 후,
        a리스트의 값들 사이에 저장하려고 한다. 
        저장조건은 a리스트의 바로 앞의 값 보다는 크고 
        바로 뒤의 값 보다는 이하인 위치에 삽입 후 출력하시오.
    [예시]
        r = 54
        a = [10,20,30,40,50,54,60]

'''
import random
a = [10, 20, 30, 40, 50, 60]

r=random.randint(1,70)
print("r=", r)

index = -1
for i in range(len(a) - 1): # a배열 -1 길이만큼 반복
    if a[i] <= r and r < a[i + 1]: # 만약 a배열 i인덱스값이 r보다 작거나 같고 a배열 i+1인덱스값보다 작으면
        index = i + 1  # 인덱스는 i+1
print("index =", index) # 인덱스 출력

if index == -1: # 인덱스가 -1이면(-1은 마지막을 의미)
    if r < a[0]: # 만약 랜덤값이 a배열 0번째인덱스의 값보다 크면 
        a.append(r) # 랜덤값을 a배열에 추가한다
        i = len(a) - 1 # i는 a배열의 길이 -1
        while i > 0: # while 반복문
            a[i] = a[i - 1] # a배열의 i인덱스값에 i-1인덱스값을 넣어준다
            i -= 1 # i -1씩 반복
        a[0] = r # a배열 0번째 인덱스에 랜덤값 추가
    else: # 그 외에는
        a.append(r) # 랜덤값 a배열에 추가
else: # 인덱스가 -1이 아니면
    a.append(r) # 랜덤값 a배열에 추가
    i = len(a) - 1 # i는 a배열의 길이 -1
    while i > index: # while 반복문 
        a[i] = a[i - 1] # a배열의 i에 값에 i-1값을 넣는다
        i -= 1 # i -1씩 반복
    a[index] = r # a배열의 index값에 랜덤값 대입
print(a)



