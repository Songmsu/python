'''
	[문제] 
  		6의 배수를 순차적으로 검사한다. 
  		그중 100에 가장 가까운 수를 출력하시오. 
 	[정답]
		102
'''
i=1
num1=0

while i<100:
	if i%6==0:
		num1=i
	i+=1
print(num1)
num2=num1+6
print(num2)

result1=100-num1
result2=num2-100

if result1<result2:
	print(num1)
if result1>result2:
	print(num2)