import fibo

print(fibo.__name__) # module name
fibo.fib(1000)
print(fibo.fib2(100))

from fibo import fib3

fib3(10)

from fibo import * # _로 시작하는 것들을 제외한 모든 이름을 import합니다.그러나 비추천합니다.

print(fib4(10))

import fibo as fff

fff.fib3(10)

from fibo import fib4 as f4f

print(f4f(1000))

# 모듈을 스크립트로 실행하기
""" 
$ python fibo.py <arguments>
모듈에 있는 코드는, 그것을 import할 때처럼 실행됩니다. 하지만 __name__은 "__main__"로 설정됩니다.

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

spam이라는 이름의 모듈이 임포트 될 때,인터프리터는 먼저 그 이름의 내장모듈을 찾습니다. 
발견되지 않으면, 변수 sys.path로 주어지는 디렉터리들에서 spam.py라는 이름의 파일을 찾습니다. 
sys.path는 이 위치들로 초기화됩니다:
"""
import sys
print(dir(fib))
# 내장함수 dir() 은모듈이정의하는이름들을찾는데사용됩니다. 문자열들의정렬된리스트를돌려줌
from tester import re
re.getter()

### """ cpython.pyc 모듈 쓰는법 알아보기"""

y = lambda x : print(x)

