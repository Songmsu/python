'''
	[문제]
		a리스트에 -100~100 사이의 랜덤 값 5개 저장한다. 
		그 중 가장 큰 수와 가장 작은 수를 출력하시오. 
	[예시]
		[37, 53, 90, -82, -17]
		90
		-82
'''

import random

a = []

for i in range(5): # -100~100 5개 랜덤 출력과정
	r = random.randint(-100, 100)
	a.append(r)
print("a =", a)

max = 0
min = 100
for i in range(len(a)): # 배열a의 길이만큼 반복
	if max < a[i]: # 만약 a[i]의 값이 max(0)보다 크면
		max = a[i] # a[i]의 값이 맥스값이 된다
	if min > a[i]: # 만약 a[i]의 값이 min(100)보다 작으면
		min = a[i] # a[i]의 값이 민값이 된다
		
print("max = ", max)
print("min = ", min)







