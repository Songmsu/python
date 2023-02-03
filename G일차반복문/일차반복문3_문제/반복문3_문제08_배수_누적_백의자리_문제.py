'''
	[문제]
	    1000~2000 사이의 숫자 중에서 
     	[1] 16의 배수 중에서 백의 자리가 7인 수만 출력하고, 
		[2] 그 합을 구하시오.
		[3] 개수를 구하시오.
    [정답]
		1712 1728 1744 1760 1776 1792 
		total = 10512
		count = 6
'''

i=1000
num=2000
count=0
total=0

while i<=num:
	if i%16==0 and i%1000//100==7:
		print(i, end=" ")
		count+=1
		total+=i
	i+=1
print()
print(total)
print(count)