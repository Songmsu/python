'''
    [문제]
        철수는 게임을 하고 있다. 
        monster는 게임의 적 4마리를 의미하고 
        숫자는 몬스터의 체력을 의미한다.
        
        철수의 공격력은 5이다.    
        총 다섯번을 반복하면서 
        랜덤으로 몬스터 중 하나를 선택해서 공격한다.
        모든 몬스터들을 공격한 후 몬스터들의 체력을 출력하시오.
        단, 몬스터 체력은 0이 되면 더 이상 내려가지 않는다.
    [예시]
        1 번째 몬스터 공격! : [9, 2, 8, 6]
        0 번째 몬스터 공격! : [4, 2, 8, 6]
        3 번째 몬스터 공격! : [4, 2, 8, 1]
        2 번째 몬스터 공격! : [4, 2, 3, 1]
        1 번째 몬스터 공격! : [4, 0, 3, 1]
'''
import random

monster = [9, 7, 8, 6]
power = 5

for i in range(5): #for 반복문 풀이
    r=random.randint(0,len(monster)-1) #0~3 반복 -> 이는 배열길이가 달라질 수 있음에 이렇게 준다

    if monster[r]-power < 0: # r번째 값에서 -5를 했을때 0보다 작으면(= -가 되면)
        monster[r]=0         # 그 r의 값은 0이다
    else:                    # 그 이외의 경우에는
        monster[r]-=power    # r의 값에서 -power(5)를 해 준다
    print(r,"번째 몬스터 공격",monster)

for i in range(5):
    r = random.randint(0, len(monster) - 1)

    if monster[r] - power < 0:
        monster[r] = 0
    else:
        monster[r] -= power
    print(r, "번째 몬스터 공격! :", monster)


