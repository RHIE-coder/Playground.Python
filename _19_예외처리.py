try:
    raise Exception('spam','eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    print('x = ', x)
    print('y = ', y)
finally:
    print("무조건이야~")


def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return())

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2,1)
print("=-==-=-==-==-=-")
divide(2,0)
print("=-==-=-==-==-=-")
divide("2","1")

