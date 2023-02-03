'''
	[문제] 
		200의 약수 중에서 짝수 중 
		80에 가장 가까운 수를 구하시오.
		만약 약수 중에 80이 있을 경우, 80이 정답이다.
	[정답]
		100
'''
i=1
num=200

first=0
second=0

while i<=num:
	if num%i==0 and i%2==0 and i<=80:
		first=i
	if num%i==0 and i%2==0 and i>80 and second==0:
		second=i
	i+=1

fresult=80-first
sresult=second-80

if fresult>sresult:
	print(second)
if fresult<sresult:
	print(first)
