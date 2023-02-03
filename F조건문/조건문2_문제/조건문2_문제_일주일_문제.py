'''
	[문제]
		이번 달 1일이 수요일이라고 할 때, 
		랜덤으로 1~31을 저장하고 해당 요일을 출력하시오.

		[예]
		3일 ==> 금요일
'''

import random
num=random.randint(1,31)
print(num,"일")

unit=num%7

if unit==1:
	print("수요일")
if unit==2:
	print("목요일")
if unit==3:
	print("금요일")
if unit==4:
	print("토요일")
if unit==5:
	print("일요일")
if unit==6:
	print("월요일")
if unit==0:
	print("화요일")