'''
	[문제]
		다음은 학생 번호와 점수의 한 세트이다.
		일등의 번호와 점수, 꼴등의 번호와 점수를 출력하시오.
	[정답]
		일등 = 1004 98
		꼴등 = 1002 11
'''


numberList = [1001, 1002, 1003, 1004, 1005]
scoreList = [87, 11, 45, 98, 23]

firstscore=0
firstindex=0

lastscore=100
lastindex=0

for i in range(len(numberList)): #넘버리스트 배열의 길이만큼 반복
	if firstscore < scoreList[i]: #scorelist 배열의 값이 firstscore보다 크면
		firstscore=scoreList[i] #firstscore의 값은 scorelist배열의 값이다
		firstindex=i # firstindex는 i
	if lastscore > scoreList[i]: #socrelist 배열의 값이 lastscore보다 작으면
		lastscore=scoreList[i] #lastscore의 값은 scorelist배열의 값이다
		lastindex=i # lastindex는 i

print("일등 :", firstindex, firstscore)
print("꼴등 :", lastindex, lastscore)
