'''
	  	[문제]
		 	아래 리스트를 아래와 같이 출력하시오.
		[결과]
			1234
			567
			89
			0
'''



a = [1,2,3,4,5,6,7,8,9,0]

first=4
last=0

for i in range(len(a)):
	print(a[i], end=" ")
	first-=1

	if first==last:
		first=4
		last+=1
		print()