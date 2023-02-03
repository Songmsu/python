'''
	[문제]
		아래 candy 리스트는 각 병에 들어있는 사탕의 양이다. 
		사탕의 종류는 전부 다르고, 한 사람 당 한 병에서 25개씩 나눠주려 한다.
		나눠 줄 수 있는 사람 수를 count 리스트에 저장하고, 나머지는 뒤로 넘겨준다.
		나눠주고 남은 사탕은 뒤로 넘겨서 합쳐서 나눠주시오.
		전부 나눠주고 난 candy와 count를 출력하시오. 
	
	[예시]
		(1) 80 : 75 개를 3명에게 나눠주고 5개 남는다. 뒤로 넘겨서 53은 58이 된다.
		(2) 58 : 50 개를 2명에게 나눠주고 8개 남는다. 뒤로 넘겨서 46은 54가 된다.
		(3) 54 : 50 개를 2명에게 나눠주고 4개 남는다. 뒤로 넘겨서 23는 27이 된다.
		(4) 27 : 25 개를 1명에게 나눠주고 2이 남는다. 
  
	[정답]
		candy = [0, 0, 0, 2]
		count = [3, 2, 2, 1]
'''

candy = [80,53,46,23]
count =[]
print("candy : " , candy)
print("count : " , count)

for i in range(len(candy)): # candy배열의 길이만큼 반복(즉 4)
	person = candy[i] // 25 # candy배열의 i인덱스값을 25로 나눈 몫을 person 변수에 저장
	count.append(person) # count 배열에 person 변수값 입력
	if i < len(candy) - 1: # 만약 i가 candy배열길이-1(3)보다 작으면,
		candy[i + 1] += candy[i] % 25 # candy배열 i+1번째 인덱스 값에 i번째 인덱스 값을 25로 나눈 나머지를 더해준다(문제에서 뒤로 넘기는 것)
		candy[i] = 0 # 넘겨주고 i번째 인덱스 값은 0이다.
	else: # 그 외에는
		candy[i] = candy[i] % 25 #candy배열 i번째 인덱스 값을 25로 나눈 나머지를 candy배열 i번째에 대입해준다.(마지막에 남은 사탕)
print(candy)
print(count)





