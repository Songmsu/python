'''
    [문제]
        [조건1] 리스트에 랜덤숫자(1~100) 5개를 추가한다.
        [조건2] 리스트의 숫자중 50보다 큰값들만 출력
        [조건3] 위조건의 값들의 누적합을 출력
        [조건4] 위조건의 개수 출력 
       
    [예시]
        a = [1, 83, 22, 77 ,19]
        비교 = 50
        출력 : 83, 77
        합 : 160
        개수 : 2
'''
import random

a = []
count = 0
total = 0
i=0
while i<5:
    r=random.randint(1,100)
    a.append(r)

    if a[i]>50:
        total+=a[i]
        count+=1
    i+=1

print(a)
print("개수 :", count)
print("총합 :", total)


