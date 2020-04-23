while True:
    try:
        x = int(input("Please enter a number : "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")

"""  
except(RuntimeError, TypeError, NameError)
    pass
"""

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B,C,D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

import sys

try:
    f = open("myfile.txt")
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error : {0}".format(err))
except ValueError:
    print("Could not convert data to an integer")
except:
    print("Unexpected error : ", sys.exc_info()[0])
    raise

print(sys.argv[0])
print(sys.argv[1])
print(type(__name__))
# 사실 is 는 == 와 달리 값을 비교하는게 아니라 레퍼런스 즉 포인터를 비교한다.
print(__name__ is '__main__')
print(__name__ == "__main__")
if __name__ == "__main__":
    print("good job")
    for arg in sys.argv[1:]:
        try:
            print("gdgd")
            f = open(arg, 'r')
        except OSError:
            print('cannot open', arg)
        else:
            print(arg, 'has', len(f.readlines()), 'lines')
            f.close()
