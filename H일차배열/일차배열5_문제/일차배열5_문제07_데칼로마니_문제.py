'''
	[문제]
		a 리스트가 데칼코마니인지 구하시오.
		데칼로마니이면 True를 출력 아니면 False 출력하시오.
		데칼코마니란? 절반으로 나눴을 때 서로 값들이 대칭이면 데칼코마니이다.

	[예시]	
		[1,5,4,4,5,1] True
		[1,5,4,3,5,1] False
'''


a = [1,5,4,4,5,1]

center=len(a)//2 # center변수에 a배열의길이 나누기2한 몫(즉 3)
count=0 # count 0주고 시작

index=len(a)-1 # index는 a배열길이에 -1(즉 5)
for i in range(center): # center 만큼 반복(즉 3)
	if a[i]==a[index]: # 만약 a배열 i인덱스값이 a배열 index인덱스값이랑 같다면
		count+=1 # 카운트 1증가
	index-=1 # index 1감소

if count==center: # 위과정을 3번 반복해서 count가 center랑 같다면
	print("True") # True 출력
else: # 그 외에는
	print("False") # False 출력