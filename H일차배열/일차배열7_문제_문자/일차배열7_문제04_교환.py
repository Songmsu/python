"""
    [문제]
        아래 리스트들은 학생들의 데이터이다. 
        학생두명의 국어 점수가 서로 바뀌어서 잘못 저장되었다. 
        랜덤으로 번호두개를 저장후 각 번호의 해당하는 국어점수를  교환후 출력하시오.

    [예시]
        1001 , 1003
        stkor = [30,20,10,40]
"""
import random

stno = [1001, 1002, 1003, 1004]
stname = ["김철수" , "이만수" , "신정아" , "이영희"]
stkor = [10 , 20 , 30 , 40]
steng = [60 , 80 , 32 , 13]
temp=0

r1=random.randint(0,len(stno)-1)
r2=random.randint(0,len(stno)-1)
print(r1, r2)
print(stno[r1], stno[r2])

temp=stkor[r1]
stkor[r1]=stkor[r2]
stkor[r2]=temp
print(stkor)