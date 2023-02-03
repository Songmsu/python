'''
   [문제]
      a리스트에 랜덤(0,3) 숫자 4개를 저장한다. 
      단, 중복없는 숫자로 저장한다.
   
   [예시]
      [1,4,2,3]
'''
import random

a = [0, 0, 0, 0] # a배열 4자리 지정

check = [False, False, False, False] # check=false 사용

count = 0
while True: #while반복문
   r = random.randint(0, 3) #0~3랜덤

   if check[r] == False: # check 배열의 r번째 인덱스 값이 false이면
      a[count] = r + 1 # a배열의 count인덱스 값이 r+1
      check[r] = True # check 배열의 r번째 인덱스 값이 True이다
      count += 1 # count 1증가

   if count == 4: # 만약 카운트가 4면
      break # 브레이크

print(a)
