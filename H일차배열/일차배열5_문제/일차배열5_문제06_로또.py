'''
	[로또]	
		아래 lotto 리스트에 1~45숫자를 순차적으로 저장한다. 
		셔플후 그중 가장앞에서 6개를 출력한다. 
'''
import random
lotto = []

for i in range(6):
	r=random.randint(1,45)
	lotto.append(r)
print(lotto)


