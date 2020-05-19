"""  
global 문은 특정 변수가 전역 스코프에 있으며 그곳에 재연결되어야 함을 가리킬 때 사용될 수 있습니다; 
nonlocal 문은 특정 변수가 둘러싸는 스코프에 있으며 그곳에 재연결되어야 함을 가리킵니다.
"""

def scope_test():
    def do_local():
        spam = "local spam"
    
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    
    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment :",spam)
    do_nonlocal()
    print("After nonlocal assignment :",spam)
    do_global()
    print("After global assignment :",spam)

scope_test()
print("In global scope :", spam)



