'''
	[문제]
		자동차 모형 28개와 로봇 모형 42개를 여러 상자에 나눠 담으려 한다. 
		각 상자마다 자동차 모형 개수와 로봇 모형 개수가 같아야 하며, 
		최대한 많은 상자에 나눠 담을 때 
		자동차 모형 몇 개와 로봇 모형 몇 개씩 넣어야 하는지 구하시오. 
	[정답]
		자동차 = 2
		로봇 = 3
'''

자동차모형=28
로봇모형=42
상자수=0

i=1
while i<=28:
	if 자동차모형%i==0 and 로봇모형%i==0:
		상자수=i
	i+=1
print(상자수)

자동차=자동차모형/상자수
로봇=로봇모형/상자수

print("자동차 :", 자동차)
print("로봇 :", 로봇)
