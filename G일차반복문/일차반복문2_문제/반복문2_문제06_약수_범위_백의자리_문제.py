'''
	[문제] 
		1000의 약수 중에서 200~800 사이 중에 
		백의자리가 5인 수만 출력하시오.
	[정답]
		500
'''

i=1
num=1000

while i<=num:
	if 200<=i and i<=800 and num%i==0 and i%1000//100==5:
		print(i)
	i+=1
