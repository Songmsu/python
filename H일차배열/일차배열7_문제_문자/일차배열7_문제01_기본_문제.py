'''
    [문제]
        문자열 hello를 olleh로 출력하시오.
'''
text = "hello"

for i in range(len(text)):
    print(text[len(text)-1-i], end="")
print()