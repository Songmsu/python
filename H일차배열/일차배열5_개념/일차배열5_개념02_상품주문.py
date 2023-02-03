'''
	[문제]
		item 리스트는 상품의 번호이다.
		price 리스트는 상품의 가격이다.
		order는 오늘 주문이 들어온 상품의 인덱스 번호이다. 
		오늘의 매출을 출력하시오.
	[정답]
		16100
'''
item  = [1001, 1002, 1003, 1004]
price = [ 500, 1200, 4300, 2300]
order = [0, 1, 3, 3, 2, 2, 1]

total = 0
for i in range(len(order)): # 주문배열의 길이만큼 반복
	total+=price[order[i]]  # 토탈에 주문번호의 가격을 더해주는 것
print(total)