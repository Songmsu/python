'''
	[문제]
		a리스트는 학생 번호와 점수 한 세트를 이루고 있다.		
		0 ~ 7 사이의 랜덤 숫자를 저장하고,
		해당 위치의 학생 번호와 그 점수를 삭제하시오.
	[예시]
		
'''
import random
a = [1001, 40, 1002, 60, 1003, 65, 1004, 70]

index=random.randint(0,len(a)-1) # index 랜덤값 지정(a배열의 길이 -1)
print("index=", index)

if index%2==0: # 인덱스가 짝수일때
    a.remove(a[index]) # 제거
    a.remove(a[index]) # 제거
else: #인덱스가 홀수일때
    a.remove(a[index]) # 제거
    a.remove(a[index-1]) #index-1의 인덱스값 제거


    
print(a)