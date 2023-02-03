'''
	[문제]
		a리스트에 랜덤(0~9) 사이의 랜덤 값을 4개 저장한 후 출력한다. 
		리스트 안의 값들이 모두 짝수면 True를 출력하고,
		하나라도 짝수가 아니면 False를 출력한다.
		단, 0은 짝수이다.
	[예시] 
		[4, 6, 2, 0] True
		[5, 2, 0, 4] False
'''

import random

a = []
for i in range(4):
	r = random.randint(0, 9)
	a.append(r)
print("a =", a)

# 방법1) count를 이용
count = 0
for i in range(len(a)):
	if a[i] % 2 == 0:
		count += 1  # 짝수일 때 count 증가

if count == len(a): # 증가한 count 개수가 a배열의 길이 즉 전부 짝수이면
	print("True")   # True 출력
else:
	print("False")  # 아니면 False 출력

# 방법2) check를 이용
check = True

for i in range(len(a)):
	if a[i] % 2 == 1:  # 랜덤숫자가 홀수일 때
		check = False  # 체크 False 를 줘서 그 외의 경우에는 True

print(check)
