'''
	[문제] 
		a리스트 안에 1 또는 7을 랜덤으로 7개 추가 후 출력하시오. 
		단, 1의 개수는 4개만 추가하고,
		7의 개수는 3개만 추가한다.
		
	[예시]
		정답 [ 1, 7, 7, 1, 1, 7, 1]  # 개수가 맞다. 
		오답 [ 7, 1, 1, 7, 1, 1, 1]  # 7이 두개이다.
			
'''
import random

'''
# 1단계
for i in range(7):
	r = random.randint(0, 1)

	if r == 0:
		a.append(1)
	elif r == 1:
		a.append(7)
'''

'''
# 2단계
cnt1 = 0
cnt7 = 0

for i in range(7):
	r = random.randint(0, 1)

	if r == 0 and cnt1 < 4:
		a.append(1)
		cnt1 += 1
	elif r == 1 and cnt2 < 7:
		a.append(7)
		cnt7 += 1
'''

a = []

cnt1 = 0
cnt7 = 0

while True:
	r = random.randint(0, 1)
	if r == 0 and cnt1 < 4:
		a.append(1)
		cnt1 += 1
	elif r == 1 and cnt7 < 3:
		a.append(7)
		cnt7 += 1

	if cnt1 + cnt7 == 7:
		break

print(a)

import random

a = []
count1 = 0
count7 = 0

while True: # while 반복문
	if count1 + count7 == 7: # 만약 count1과 count7의 합이 7이면
		break # break로 반복문 종료

	r = random.randint(0, 1) # 0 또는 1 랜덤값 추출

	if r == 0 and count7 < 3: # 만약 랜덤값이 0이고 count7의값이 3보다 작으면
		a.append(7) # a배열에 7의 값 추가
		count7 += 1 # count7 1 증가
	elif r == 1 and count1 < 4: # 만약 랜덤값이 1이고 count1의값이 4보다 작으면
		a.append(1) # a배열에 1의 값 추가
		count1 += 1 # count1 1 증가
print(a)



    
