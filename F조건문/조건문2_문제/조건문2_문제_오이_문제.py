'''
	[문제]	  	
		마트에서 오이를 3개씩 묶어서 1500원에 판매한다.
		오이가 14개 필요하다면,
		필요한 금액을 출력하시오.
		단, 오이는 묶음으로만 판매한다.
	[정답]
		7500
'''

한묶음=1500
오이개수=14
묶음수량=오이개수//3

if 오이개수%3 != 0:
	묶음수량=묶음수량+1
print(묶음수량)

금액=묶음수량*한묶음
print(금액)