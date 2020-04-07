# 주석은 "#"을 사용하여 선언합니다.
varNum = 1 # 이렇게 옆에서 설명할 수 도 있고
                         # .. 이런식으로.내용을 이어서 설명하세요.

#===== print()  =====#
print("이곳에 들어온 데이터를 console에 출력해주는 함수 print()")

#===== 숫자 =====#
#   +: 더하기
print("10+20=",10+20)

#   -: 빼기
print("30-10=",30-10)

#   *: 곱하기
print("5*5=",5*5)

#   /: 나누기(몫)
print("10/3=",10/3) #항상 float를 돌려준다.

#   //: 나누기(몫 - 정수)
print("10//3=",10//3) # 소수부 없이 정수의 결과

#   %: 나누기(나머지)
print("10%3=",10%3)

#   **: 거듭제곱
print("10**2=",10**2)

#===== 변수 =====#
num = 10 # num은 변수, 10은 변수의 값입니다. 
                    # ...수학적으로는 좌변과 우변이 같다는 표시지만
                    # ...프로그래밍에선 우측에 있는 자료를 좌측에 있는 num이라는 그릇에  담는다는 뜻입니다.
text = "# 이런식으로 표현한건 주석이 아니라 문자열입니다."

print("num*10=",num*10)
#print(numVar) #NameError: name 'numVar' is not defined
# 선언되어있지 않은 변수를 사용하게되면 에러가 발생한다.

num = 20 # 이미 num이 선언되었는데도 불구하고 다시 선언이 된다.
print("다시 선언된 num :",num)

#===== 문자열 =====#
print("문자열이 이곳에 들어간다.")  # 문자열은 ("  ")사이의 값이고, (")은 프로그래밍을 위해 약속된 예약어이다.
                                                                         # ... 만일 (")를 문자로 표현하고 싶으면 어떻게할까?
                                                                         # ... 이스케이프라는 개념이 있다!!!
print("문자열이 \"이곳\"에 들어간다.") # (\)를 사용하면 된다.
print('\'이런\'식의 사용도 가능하다.') # 문자열을 표현할 때 (' ')를 사용할 수도 있다. 역시 (\)를 사용하면 작은따옴표(') 표현 가능
print("이스케이프n 사용 : 안녕\n하\n세요") # 예약어인 특수 문자를 표현할 때 뿐만아니라 개행(new line)과 같은 동작도 가능
print("이스케이프t 사용 : 안녕하\t세요") # (\t)는 tab효과를 넣어준다.(8칸)
                                                            #만일 -->  C:\Users\name\python <-- 이런식으로 표현하고 싶다면 (\n)이 동작하게 된다.
print(r"파일경로 : C:\Users\name\python") # ... 이때는 r (raw String)을 문자열 앞에 붙여주면 된다.
# 여러 줄로 한번에 표현할 수도 있다.
strings = """
사용법 : cd [path]
    . : 현재 위치
    .. : 이전 위치
"""
print(strings) # (''')를 사용해도 같은 결과를 얻는다
# 여러 줄의 문자열이 시작될때 첫줄이 개행되는걸 볼 수 있는데 (\)을 붙여주면 해결된다.

strings2 = '''\
    여러줄의 문자 리터럴은 
    삼중 따옴표로 표현해보세요



    간단~!
'''
print("=============")
print(strings2)
print("=============")

joinString = 'Hello '  "World" # 두 개 이상의 문자 리터럴이 연속으로 나타나면 자동으로 붙여짐, 문자가 길 때 유용함
print(joinString)

prefix = "Py"
#print(prefix "thon") #SyntaxError: invalid syntax
#그러나 변수와 리터럴이 연속이면 해당되지 않습니다. 이때는 (+)를 사용해야합니다.
print(prefix+"thon")
print("STRING " * 5) # (*)연산자로 반복시킬 수도 있습니다.

# 문자열은 인덱싱도 가능하다.
word = "abcde"
print("word[2] :",word[2])
print("word[-1] :",word[-1]) # 음수도 가능하다니... 
print("word[2:4] :",word[2:4] ) # characters from position 2 (included) to 4 (excluded)
print("word[:2] + word[2:] =",word[:2] + word[2:]) # 시작 위치의 문자는 항상 포함되는 반면, 종료 위치의 문자는 항상 포함되지 않는 것에 주의

# 파이썬의 문자열은 Immutable
#word[0] = "F" #TypeError: 'str' object does not support item assignment

# 문자열의 길이
print("문자열의 길이 :", len(word))
