'''
[문제]
	철수는 볼펜을 (10~30)개를 구입해야 한다. 
	
	볼펜 하나의 가격은 1200원이다. 	
	볼펜은 20개 이상 구매 시 볼펜 한 개에 100원을 할인해주고 있다. 
		
	또한, 회원 등급에 따라 할인을 추가 제공한다.
	
	회원 등급이 1이면 15% 할인제공, 단, 20개 이상이면 1100에서 15% 할인
	회원 등급이 2이면 10% 할인제공, 단, 20개 이상이면 1100에서 10% 할인
	기본회원 등급은 3이고 할인을 제공하지 않는다.
	
	볼펜 수를 랜덤으로 저장한다.
	회원 등급을 랜덤으로 저장한다. 
	
	철수가 지급해야 하는 금액을 출력하시오.
'''
import random
볼펜=random.randint(10,30)
print("볼펜:", 볼펜)
등급=random.randint(1,3)
print("등급:", 등급)

볼펜가격=1200

if 볼펜>=20: 
	볼펜가격=1100

할인율=0
if 등급==1:
	할인율=0.15
if 등급==2:
	할인율=0.1
금액=볼펜*볼펜가격*(1-할인율)
print(금액)
