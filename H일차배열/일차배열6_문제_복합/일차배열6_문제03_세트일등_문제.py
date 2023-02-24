'''
	[문제]
		a리스트는 학생 번호와 점수 한 세트를 이루고 있다.		
		일등 학생의 번호와 점수를 출력하시오.
	[정답]
		번호 = 1002
		점수 = 82
'''
a = [1001, 40, 1002, 82, 1003, 65, 1004, 70]

maxscore=0
maxindex=0

for i in range(len(a)): # a배열의 길이만큼 반복
    if i%2==1: # 홀수번째 값
        if maxscore < a[i]: # a배열의 i인덱스값이 maxscore(0)보다 크면
            maxscore=a[i] # maxscore에 a배열의 i인덱스값을 넣어준다
            maxindex=i # maxindex는 i의값을 넣어준다
            
print(a[maxindex-1], maxscore) # 출력