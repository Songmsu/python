'''
	[문제]	
		아래 리스트 a의 값을 사각형 모양으로 출력하시오.
	[예시]
		1 2 3 
		4 5 6 
		7 8 9 
'''

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
0 1 2
3 4 5
6 7 8
'''

# 방법1) count를 사용한다
count = 0
for i in range(len(a)):
	print(a[i], end=" ")
	count += 1

	if count == 3: # count가 3이되면
		print()  # 줄바꿈을 해주고
		count = 0 # 다시 count를 0으로
print()

# 방법2)
for i in range(len(a)):
	print(a[i], end=" ")
	if i % 3 == 2: # i값을 3으로 나눈 나머지가 2이면
		print() # 줄바꿈


