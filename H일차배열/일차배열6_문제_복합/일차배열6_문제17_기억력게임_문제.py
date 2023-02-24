'''
     [문제]
      1. 같은 숫자가 적혀있는 카드 2장씩 5세트가 있다. (총10장)
      2. front는 카드를 엎어놓은 상태를 뜻한다. 
      3. 먼저 front를 셔플한다. 
      4. front에 있는 카드 2개를 랜덤으로 선택한다. (마우스가 없으므로 인덱스로 선택)
      5. 선택한 카드 2장의 내용이 같으면 back에 복사해서 맞춘 걸 표시한다. 
         back에 모든 글자가 채워지면 게임은 종료된다.
         
      6. 같은 인덱스 선택할 수 없다. 
      7. 이미 선택한 자리를 또 선택할 수 없다. 
'''
import random

front = [10,10,20,20,30,30,40,40,50,50]
back = [0,0,0,0,0,0,0,0,0,0]


for i in range(100):
    idx1=random.randint(0, len(front)-1)
    idx2=random.randint(0, len(front)-1)

    temp=front[idx1]
    front[idx1]=front[idx2]
    front[idx2]=temp

count=0
while True:
    if count == len(front)//2:
        break
    
    idx1=random.randint(0, len(front)-1)
    idx2=random.randint(0, len(front)-1)
    print(idx1, idx2)

    if idx1 != idx2:
        if back[idx1]==0 and back[idx2]==0 and front[idx1]==front[idx2]:
            back[idx1]=front[idx1]
            back[idx2]=front[idx2]
            count+=1

            print("front=", front)
            print("back=",back)