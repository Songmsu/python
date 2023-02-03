'''
	  	[문제]
		 	아래 리스트를 아래와 같이 출력하시오.
		[결과]
			1
			23
			456
			7890
'''

a = [1,2,3,4,5,6,7,8,9,0]

first = 0
last = 1

for i in range(len(a)):
    print(a[i], end=" ")
    first += 1

    if first == last: # 만약 둘이 같아 진다면
        first = 0 # first는 다시 0
        last += 1 # last는 1증가
        print() # 줄바꿈
