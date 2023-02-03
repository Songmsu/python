'''
    [문제]
        [조건1] 배열에 랜덤숫자(1~100) 5개를 추가하고,
        [조건2] 짝수만 출력하시오.
        [조건3] 짝수의 누적 합을 저장 후 출력하시오.
        [조건4] 짝수의 개수를 출력하시오.
    
    [예시]
        arr = [68, 81, 84, 72, 81]
        68
        84
        72

        개수 = 3
        합 = 224
'''

import random

count=0
total=0
arr = []

i=0
while i<5:
    r=random.randint(1,100)
    arr.append(r)

    if arr[i]%2==0:
        print(arr[i])
        count+=1
        total+=arr[i]
    i+=1

print(total)
print(count)
