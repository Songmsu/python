'''
    [문제]  
        아래 a리스트는 순서대로 값이 저장되어있다.
        랜덤(1~100)숫자 하나를 저장 후,
        랜덤 값보다 작은 값은 전부 a리스트에서 삭제하시오.
    [정답]

'''
import random 
a = [10, 20, 30, 40, 50, 60]
r=random.randint(1,100)
print(r, end=" ")

i=0
while True: # while 반복문 사용
    if i==len(a): # 만약 i가 a배열의길이와 같다면
        break # break 로 반복문 종료
    if a[i]<r: # 만약 a배열이 i인덱스값이 r보다 작다면
        a.remove(a[i]) # a배열에서 i인덱스값 제거
        i-=1 # i값 1감소
    i+=1 # i값 증가를 통한 반복문
print(a)