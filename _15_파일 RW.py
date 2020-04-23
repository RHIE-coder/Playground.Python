# 파일을 읽고 쓰기
"""  
open()은 파일 객체를 돌려주고, 두 개의 인자를 주는 방식이 가장 많이 사용됩니다. open(filename, mode)
f = open('workfile','w')
r : read
w : write --> 이미 존재하는 것은 삭제
a : 파일을 덧붙이기 위해 엽니다.
r+ : 파일을 읽고 쓰기위해
mode를 생략하면 r
b : binary file, 텍스트를 포함하지 않는 모든 파일에는 이 모드를 사용해야 합니다.
텍스트 모드에서 읽을 때의 기본 동작은 플랫폼 의존적인 줄 종료(유닉스 \n, 윈도우 \r\n)를 단지 \n으로 변경하는 것입니다.
"""
"""  
파일 객체를 다룰 때 with 키워드를 사용하는 것은 좋은 습관입니다. 혜택은 도중 예외가 발생하더라도
스위트가 종료될 때 파일이 올바르게 닫힌다는 것입니다. with 를 사용하는 것은 동등한 try-finally
블록을 쓰는 것에 비교해 훨씬 짧기도 합니다
"""

with open("sample.txt", "w") as f:
    f.write("It's simple code\n")
    f.write("and the test for file system api")

"""
위 코드는 close함수가 없지만 with as 구문을 빠져나가게 되면 자동으로 close() 함수를 호출하여 파일을 닫습니다. 
with as 구문은 이처럼 파일 스트림을 손쉽게 다루는 경우에 유용하지만 네트워크 스트림을 다루는 소켓 프로그래밍과 같은 곳에서도 활용할 수 있습니다.
"""
with open("sample.txt") as f:
    for line in f:
        print(line, end='')

print("\n==========================")

with open("sample.txt") as f:
    print(f.readlines()) #list형태로

print()

value = ('the answer', 42)
s = str(value)
print(type(s), s)

"""  
f.tell() 은 파일의 현재 위치를 가리키는 정수를 돌려주는데, 바이너리 모드의 경우 파일의 처음부터의
바이트 수로 표현되고 텍스트 모드의 경우는 불투명한 숫자입니다.
"""
f = open("sample.txt","r")
print({1})
print(f.tell())
print({2})
print(f.readline())
print({3})
print(f.tell())
print({4})
print(f.readline())
print({5})
print(f.tell())
f.close()


with open("sample.txt","rb+") as f:
    print(f.write(b'0123456789abcdef'))
    print(f.seek(10))
    print(f.tell())
    print(f.read(2))

# assert 디버깅 목적으로 사용됩니다.
a = 10
assert a > 5
assert a < 5, "a의 값이 너무 큽니다."

