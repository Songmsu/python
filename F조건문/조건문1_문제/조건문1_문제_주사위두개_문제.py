'''
    [문제]
        철수는 주사위 2개를 가지고 있다.
        주사위는 눈금이 1~6까지 있다.
        철수가 주사위 2개를 던졌을 때 그 합을 출력하시오.
        단, 주사위 눈금이 서로 같으면 6을 추가로 더하시오.

        [예]
            1, 2 ==> 3
            1, 1 ==> 2 + 6
'''

import random
a=random.randint(1,6)
b=random.randint(1,6)

print(a, b)
if a==b:
    print(a+b+6)
if a!=b:
    print(a+b)