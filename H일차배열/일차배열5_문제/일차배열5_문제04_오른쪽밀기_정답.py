'''
	[문제]
		a리스트의 값중 0을 제외하고 모든값을 오른쪽으로 모으시오.
 	[결과]
 		a = [0,0,0,0,0,0,2,3,4,5];
'''


a = [0,0,2,0,3,0,4,0,0,5]


j = len(a) - 1 #9
idx = len(a) - 1 #9
for i in range(len(a)): #a배열 길이만큼 반복
	if a[j] != 0: #a[9]값이 0이 아니면
		temp = a[idx] #temp에 a[idx]값 대입
		a[idx] = a[j] #a[idx]에 a[j]값 대입
		a[j] = temp #a[j]에 temp값 대입

		idx -= 1 # 한번 반복 시 idx값 -1
	j -= 1 # j를 -1반복
print(a)
