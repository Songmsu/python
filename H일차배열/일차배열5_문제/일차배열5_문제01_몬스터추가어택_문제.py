'''
    [문제]
        철수는 게임을 하고 있다. 
        monster는 게임의 적 4마리를 의미하고 9는 몬스터의 체력을 의미한다.
        철수의 공격력은 5이다.     
        랜덤으로 몬스터 중 하나를 선택해서 공격하고,
        이를 총 다섯 번 반복한다. 
        모든 몬스터를 공격한 후 몬스터들의 체력을 출력하시오.
        단, 몬스터 체력은 0이 되면 더 이상 내려가지 않는다. 
        또한 공격한 몬스터의 양쪽에게는 1의 대미지를 가하게 된다. 
        
'''
import random
monster = [9,7,8,6]
power = 5

count=0
while True: # while 반복문
    if count==5: # 만약 카운트가 5가되면
        break # break로 멈춤
    r=random.randint(0,len(monster)-1) # 랜덤값 r(0~3)
    if monster[r] > 0: # 만약 monster배열이 0보다 크면
        if monster[r]-power<0: # 만약 monster배열이 0보다 클때 monster배열값에서 -5했을때 0보다 작으면(즉 -이면)
            monster[r]=0 # r번째 인덱스 monster의 값은 0이다.
        else: # 그 외의 경우에는
            monster[r]-=power # r번째 인덱스 monster의 값에서 -5
        
        #왼쪽 -1
        if monster[r-1]>0 and r>0: # 만약 r-1번째 인덱스 monster의 값이 0보다 크고, r이 0보다 클때
            if monster[r-1]-1<0: # r-1번째 인덱스 monster 값에서 -1을 했을때 0보다 작으면(즉 음수이면)
                monster[r-1]=0 # r-1번째 인덱스 monster값은 0이다.
            else: # 그 외에는
                monster[r-1]-=1 # r-1번째 인덱스 monster 값에서 -1

        #오른쪽 -1
        if r < len(monster)-1 and monster[r+1] > 0: # r이 len(monster)-1 즉3보다 작고, r+1번째 인덱스 monster의 값이 0보다 크면
            if monster[r+1]-1<0: # r+1인덱스 monster 값에서 -1을 했을때 0보다 작다면(즉 음수)
                monster[r+1]=0 # r+1인덱스 monster의 값은 0이다
            else: #그 외에는(0보다 크면)
                monster[r+1]-=1 #r+1인덱스 monster 값에서 -1
        count+=1 # 이 과정이 끝나면 count +1
        print(r,"번째 몬스터 공격",monster)
