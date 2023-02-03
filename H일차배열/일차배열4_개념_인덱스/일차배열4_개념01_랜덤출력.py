'''
    [문제]
        [조건1] 리스트에 랜덤숫자(1~100) 5개를 추가하고,
        [조건2] 랜덤으로 위 값 중 한 개만 출력하시오. 
    
    [예시]
        a = [1, 43, 22, 77 ,44]
        출력 : 22
'''
import random

a = []

for i in range(5):
    r = random.randint(1, 100)
    a.append(r)
print("a =", a)  #a배열안에 5개의 랜덤값 넣고 출력하는 과정

index = random.randint(0, len(a) - 1) #index를 랜덤으로 뽑는 과정
print("index =", index) #인덱스 값 출력

print(a[index]) #a배열의 랜덤 인덱스에 해당하는 값 출력




