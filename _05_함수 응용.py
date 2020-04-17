def standard_arg(arg):
    print(arg)

# 3.8 버전부터
# def pos_only_arg(arg, /):
#     print(arg)


# 두 번째 함수 pos_only_arg는 함수 정의에 /가 있으므로 위치 매개 변수만 사용하도록 제한됩니다:
"""
    >>> pos_only_arg(1)
    1

    >>> pos_only_arg(arg=1)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: pos_only_arg() got an unexpected keyword argument 'arg'
"""


def kwd_only_arg(*, arg):
    print(arg)


# 마지막은 같은 함수 정의에서 세 가지 호출 규칙을 모두 사용합니다:
# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only)


standard_arg(2)
standard_arg(arg=2)
# kwd_only_arg(3) 세 번째 함수 kwd_only_args는 함수 정의에서 *로 표시된 키워드 인자만 허용합니다:
kwd_only_arg(arg=3)


# 인자 목록 언 패킹
print(list(range(3, 6)))
args = [3, 6]
print(range(*args))  # 위랑 똑같은 결과


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
print(*d)
# print(**d) --> keyword 매개 변수를 넣을 때 쓴다.
parrot(*d)
parrot(**d)
