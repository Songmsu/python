'''
	[문제] 
		numberList 는 학생들의 번호를 저장한 리스트이다.
		scoreList 는 학생들의 점수를 저장한 리스트이다.
 		실수로 학생들의 점수가 한 칸씩 밀렸다. 
		학생들의 점수를 한 칸씩 앞으로 당기고 
		맨 앞의 점수는 맨 뒤에 저장하시오.
	
	[정답]	
		[ 1001, 1002, 1003, 1004, 1005 ]
		[ 11, 45, 98, 23, 87 ]
'''

numberList = [1001, 1002, 1003, 1004, 1005]
scoreList =  [87, 11, 45, 98, 23]

num=scoreList[0] # 맨 앞 점수 num변수에 저장

for i in range(len(numberList)-1): # 넘버리스트배열의 길이 -1 만큼 반복
	scoreList[i]=scoreList[i+1] # 넘버리스트 배열의 i에 i+1 저장
scoreList[len(scoreList)-1]=num # 아까 저장해둔 num변수 대입 
print(scoreList)
