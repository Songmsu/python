'''
	[문제]	  
		[1] 10000~90000 사이의 랜덤 숫자 저장한다.
		[2] 두 번째 자리와 네 번째 자릿수의 합을 출력하시오.

		[예]
			랜덤숫자 : 45343

			두 번째 자릿수 : 5
			네 번째 자릿수 : 4
			합 : 9
'''
import random
num=random.randint(10000,90000)
print(num)

두번째=num%10000//1000
네번째=num%100//10
print(두번째, 네번째)
print(두번째+네번째)
