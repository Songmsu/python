'''
	[문제]
		철수와 민수는 같은 수영장에 다닌다.
		철수는 4일마다 한 번씩 가고 민수는 5일마다 한 번씩 간다.
		
		철수와 민수가 2월 3일 처음 만났다면 
		다음에 서로 만나는 날은 언제인가?
	[정답]
		23
'''

철수=4
민수=5

일=3

i=1
run=1
while run==1:
	if i%철수==0 and i%민수==0:
		일=일+i
		run=0
	i+=1
print(일)