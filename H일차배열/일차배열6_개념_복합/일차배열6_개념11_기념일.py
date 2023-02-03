'''
	[문제]	
		철수와 영희는 3월 3일에 만났다. 		
		철수는 영희와 100일 기념일에 축하 파티를 하려 한다.
		만난 지 100일 뒤는 몇 월 며칠인지 구하시오.
		단, 윤년은 계산하지 않으며,
		시작일은 포함시키지 않는다.
	[정답]
		6월 11일
'''

monthList =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = 3
day = 3

total = 0
for i in range(month - 1): # month-1만큼 반복(2)
	total += monthList[i] # total +[0]31 +[1]28
total += day # 31+28+3
print("total =", total) # 62

total += 100 # 62+100
print("total =", total) #162

i = 0
while True: #while 반복문
	temp = total # 변수temp에 total값 입력
	total -= monthList[i] # total -monthlist배열 값
	if total < 0 : # 만약 total의 값이 0보다 작다면(즉 음수)
		print((i+1), temp) # i+1 , temp값 출력
		break # break로 반복문 종료
	i += 1 # i값 1증가 
	



