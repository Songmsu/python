'''
	[문제]
		a리스트에 랜덤(0 ~ 100) 사이의 랜덤 값을 4개 저장한 후 출력한다. 
		배열의 값은 학생들의 성적이다. 
		60점 이상이면 합격이다. 
  		전원합격 시 "상품" 을 출력. 
		전원탈락 시 "벌칙" 를 출력.
		그 외는 리스트만 출력하시오.
		
		[예시] 
			[67, 100, 98, 97] "상품"
			[53, 25, 12, 41] "벌칙"
'''
import random
a = []

for i in range(4): #r랜덤 반복을 통해 4개 출력과정
	r=random.randint(0,100)
	a.append(r) # 랜덤값r을 a배열에 추가
print(a)

count1=0
count2=0
for i in range(len(a)):
	if a[i]>=60: #60점이상 카운트
		count1+=1
	if a[i]<60: #60점미만 카운트
		count2+=1

if count1==4: 
	print("상품")
elif count2==4:
	print("벌칙")
