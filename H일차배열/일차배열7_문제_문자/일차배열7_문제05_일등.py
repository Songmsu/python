"""
    [문제]
        아래 리스트들은 학생들의 데이터이다. 
        학생두명의 국어 점수가 서로 바뀌어서 잘못 저장되었다. 
        랜덤으로 번호두개를 저장후 각 번호의 해당하는 국어점수를  교환하시오.
        그리고 교환한후에 국어점수와 영어점수의 총합이 1등인 학생의 이름을 출력하시오.
"""
import random

stno = [1001, 1002, 1003, 1004]
stname = ["김철수" , "이만수" , "신정아" , "이영희"]
stkor = [8 , 25 , 34 , 40]
steng = [60 , 30 , 32 , 23]

temp=0

r1=random.randint(0,len(stno)-1)
r2=random.randint(0,len(stno)-1)
print(r1, r2)
print(stno[r1], stno[r2])

temp=stkor[r1]
stkor[r1]=stkor[r2]
stkor[r2]=temp
print(stkor)

maxscore=0


for i in range(len(stno)):
    sumscore=stkor[i]+steng[i]
    if maxscore < sumscore:
        maxscore=sumscore
print(stname[i], maxscore)
