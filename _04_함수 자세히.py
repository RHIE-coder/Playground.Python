def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
# ask_ok(10)

i = 5

def f(arg=i):
    print(arg)
i = 6

f()

def f2(a, L=[]):
    L.append(a)
    return L

print(f2(1))
print(f2(2))
print(f2(3)) # 기본값은 오직 한 번만 값이 구해지고, 공유된다.

def f3(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f3(1))
print(f3(2))
print(f3(3))

"""
키워드 인자
"""

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    print("=====")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keywor

#하나의 필수 인자(voltage)와 세 개의 선택적 인자 (state, action, type) 를 받아들입니다.

# **name 형식의 마지막 형식 매개변수가 존재하면, 
# 형식 매개변수들에 대응하지 않는 모든 키워드 인자들을 담은 딕셔너리{}를 받습니다.
# 이것은 *name 형식의 형식 매개변수와 조합될 수 있는데, 
# 형식 매개변수 목록 밖의 위치 인자들을 담은 튜플을 받습니다.
# *name은 **name 앞에 나와야 합니다.

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


