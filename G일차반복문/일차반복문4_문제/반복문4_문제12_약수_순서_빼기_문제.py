'''
	[문제] 
		100의 약수 중에서 
        5번째 약수에서 2번째 약수를 뺀 값을 구하시오.
	[정답]
		8
'''
i=1
num=100
five=0
two=0
count=0

while i<=num:
	if num%i==0:
		count+=1
		if count==2:
			two=i
		if count==5:
			five=i
	i+=1

result=five-two
print(result)
