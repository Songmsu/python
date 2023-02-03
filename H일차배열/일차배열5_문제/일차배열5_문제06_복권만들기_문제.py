'''
	[문제] 
		a리스트 안에 1 또는 7을 랜덤으로 7개 추가 후 출력하시오. 
		단, 7의 개수는 3개만 추가하고, 1의 개수는 4개만 추가한다.
		위에서 만든 복권을 판정한다. 
  		7이 연속으로 3개면 "당첨"을 출력한다.
		아니면 "꽝"을 출력한다.
		
	[예]
		[ 1, 7, 7, 1, 1, 7, 1]  "꽝"
		[ 1, 1, 1, 7, 7, 7, 1]  "당첨"
'''

import random
lotto = []

count1 = 0
count7 = 0

while True: #while 반복문
    if count1+count7 == 7: # count1+count7이 7이면
        break # break로 종료
    r = random.randint(0, 1) # 0,1 랜덤
    if r == 0 and count1 < 4: # 랜덤값 r이 0이고 count1의값이 4보다 작으면
        lotto.append(1) # lotto 배열에 1 추가
        count1 += 1 # count1 1증가
    elif r == 1 and count7 < 3: # 랜덤값 r이 1이고 count7의값이 3보다 작으면
        lotto.append(7) # lotto 배열에 7 추가
        count7 += 1 # count7 1증가
print(lotto) # lotto배열 출력

check = False # check false 사용
count = 0 # 카운트 변수
for i in range(7): # 7번반복
    if lotto[i] == 7: #lotto 배열 i인덱스값이 7이면
        count += 1 # count 1증가

        if count == 3: # 만약 count가 3이면
            check = True # check true
    else: # 그 외에는
        count = 0 # count는 0이다

if check == True: # 만약 check가 true이면
    print("당첨") # 당첨 출력
else: # 그 외에는
    print("꽝") # 꽝 출력
