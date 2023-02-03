'''
	[문제]
		철수는 마블 게임을 하고 있다.
		map리스트는 철수가 움직일 수 있는 공간을 리스트로 표현한 것이다.
		숫자 1은 철수의 현재 위치를 의미한다.

		주사위(1~6)를 던져서 랜덤숫자만큼 1을 전진시킨다. 	
		만약 1이 끝까지 도달하면 다시 맨 앞으로 이동해서 전진한다.
		총 4회 반복하면서 철수의 위치를 출력하시오.
	[예시]
		(1) 시작
			map = [1,0,0,0,0,0,0,0,0,0]
		
  		(2) 주사위 : 5
			map = [0,0,0,0,0,1,0,0,0,0]

		(3) 주사위 : 3
			map = [0,0,0,0,0,0,0,0,1,0]
   
		(4) 주사위 : 6
			map = [0,0,0,0,1,0,0,0,0,0]
   
		(5) 주사위 :4
			map = [0,0,0,0,0,0,0,0,1,0]

'''

import random

map = [1,0,0,0,0,0,0,0,0,0]
print(map)

position = 0

for i in range(4): #4번반복
	move = random.randint(1, 6) #move가 1~6주사위

	map[position] = 0 #map배열의 position인덱스는 0이다

	position += move # position에 랜덤값 move를 더해준다
	position %= len(map) # position을 len(map)으로 나눈다음 그 값을 position에 대입

	map[position] = 1 # map배열의 position인덱스는 1이다

	print(move, map)
