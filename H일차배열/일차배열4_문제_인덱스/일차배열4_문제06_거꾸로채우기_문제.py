'''
	[문제]
		공간이 10개인 a리스트가 있다. 
		랜덤(0~9)로 시작 인덱스를 저장한다.
		랜덤(1~10)로 개수를 저장한다.
		시작 인덱스부터 개수만큼 거꾸로 숫자를 채워나간다.
		채우는 숫자는 1부터 1씩 증가한다.
		
	[예시]
		ranIndex = 3 
		ranCount = 7		
  		a = [4,3,2,1,0,0,0,7,6,5]  
  			- 인덱스 3부터 7개를 채운다. 
	

'''
import random
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

index=random.randint(0,9)
print("index=", index)
count=random.randint(1,10)
print("count=", count)

num=1
for i in range (count): # count의 값만큼 반복
	a[index]=num # 랜덤index의 값에 변수num(1) 저장
	index-=1 # 인덱스값 반복마다 -1
	num+=1 # 변수값 반복바다 +1
	if index < 0: # 인덱스의값이 0보다 작아지면(즉 -가되면)
		index=len(a)-1 # 인덱스는 a배열의길이-1로 돌아간다
print(a)
