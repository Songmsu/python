'''
    [문제] 다음 조건이 전부 맞는 수를 출력하시오.		
        [조건1] 13의 배수를 전부 검사한다.
        [조건2] 그중 6번째 배수에서 4번째 배수를 뺀 수를 구한다.	
        4번째는 배수는 52, 6번째 배수는 78이다.
    [정답]       
        26
'''
'''
    [설명]
        아래 식은 카운트를 한 번만 사용하는 것이 아니라 
        두 번 사용한 경우이다.
'''

i=1
run=1
num1=0
num2=0
count=0

while run==1:
    if i%13==0:
        print(i, end=" ")
        count+=1
        if count==4:
            num1=i
        if count==6:
            num2=i
            run=0
    i+=1
print()
result=num2-num1
print(result)

