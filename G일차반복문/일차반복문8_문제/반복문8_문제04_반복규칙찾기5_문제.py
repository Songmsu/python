'''
	[문제]
	  	반복문을 10회 반복해서 아래와 같이 출력하시오.
		[예시]
			0 0
			1 0
			2 1
			3 1
			4 2
			5 2
			6 3
			7 3
			8 4
			9 4
'''

a=0
b=0

i=0
while i<10:
	print(a,b)

	a+=1
	if i%2==1:
		b+=1
	i+=1