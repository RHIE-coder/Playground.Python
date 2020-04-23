"""  
패키지를 import할 때, 파이썬은 sys.path에 있는 디렉터리들을 검색하면서 패키지 서브 디렉터리를 찾습니다.
파이썬이 디렉터리를 패키지로 취급하게 만들기 위해서 __init__.py파일이 필요합니다.
"""
# from game.sound.echo import echo_test
# echo_test()

"""  
하지만 다음과 같이 echo_test 함수를 사용하는 것은 불가능하다.
import game
game.sound.echo.echo_test()
    -    AttributeError: 'module' object has no attribute 'sound'

import game을 수행하면 game 디렉터리의 모듈 또는 game 디렉터리의 __init__.py에 정의한 것만 참조할 수 있다.
또 다음처럼 echo_test 함수를 사용하는 것도 불가능하다.
import game.sound.echo.echo_test
"""

from game.sound import *
echo.echo_test()
"""
여기에서 __all__이 의미하는 것은 sound 디렉터리에서 * 기호를 사용하여 import할 경우 이곳에 정의된 echo 모듈만 import된다는 의미이다.
"""
"""relative 패키지
만약 graphic 디렉터리의 render.py 모듈이 sound 디렉터리의 echo.py 모듈을 사용하고 싶다면 어떻게 해야 할까? 다음과 같이 render.py를 수정하면 가능하다.

from game.sound.echo import echo_test
def render_test():
    print ("render")
    echo_test()
"""
from game.graphic.render import render_test
render_test()