'''
    [문제]
        1부터 100 사이의 숫자 두 개를 랜덤으로 저장한다.
        두 숫자 중 더 큰 숫자를 출력하시오.
        단, 서로 같으면 "같다"를 출력하시오.
'''
import random
a=random.randint(1,100)
b=random.randint(1,100)
print(a, b)

if a>b:
    print(a)
if a<b:
    print(b)
if a==b:
    print("서로 같다")
