'''
	[문제]
		a리스트의 각 값이 a리스트 전체의 본인 값에서 
		나머지 값을 모두 뺀 값을 total에 저장하시오.
	[예시]
		10 에서 나머지 값들 20, 30, 40 을 전부 뺀다. total = [-80]
		20 에서 나머지 값들 10, 30, 40 을 전부 뺀다. total = [-80, -60]
		30 에서 나머지 값들 10, 20, 40 을 전부 뺀다. total = [-80, -60, -40]
		40 에서 나머지 값들 10, 20, 30 을 전부 뺀다. total = [-80, -60, -40, -20]
    [정답]
        [-80, -60, -40, -20]
'''
a = [10, 20, 30, 40]
total = []

for i in range(len(a)):
    score=0
    for j in range(len(a)):
        if i != j:
            score+=a[j]
    result=a[i]-score
    total.append(result)

print(total)


