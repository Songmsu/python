'''
	[문제]
		[조건1]  30의 약수를 출력하고 
  		[조건2]  전체 합을 구하시오.
		[조건3]  개수를 구하시오.

	[정답]	
		1 2 3 5 6 10 15 30
		total = 72
		count = 8
'''
i=1
num=30
count=0
total=0

while i<=num:
	if num%i==0:
		count+=1
		total+=i
		print(i, end=" ")
	i+=1
print()
print("총합 =", total)
print("개수 =", count)

