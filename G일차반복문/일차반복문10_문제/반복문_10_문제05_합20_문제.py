'''
    [문제]
        1~10 사이의 랜덤 숫자 3개 저장하고
        그 숫자의 합이 무조건 20이 되도록 출력해보자.
'''

import random


run=1
while run==1:
    a=random.randint(1,10)
    b=random.randint(1,10)
    c=random.randint(1,10)

    total=a+b+c
    if total==20:
        run=0
print(a,b,c)