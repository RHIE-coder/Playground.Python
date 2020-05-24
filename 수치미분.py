import numpy as np


def func(input_obj):
    w = input_obj[0, 0]
    x = input_obj[0, 1]
    y = input_obj[1, 0]
    z = input_obj[1, 1]
    return (w*x + x*y*z + 3*w + z*np.power(y, 2))


def numericalDerivative(f, x):
    deltaX = 1e-4
    print("deltaX : ", deltaX)
    coefficient = np.zeros_like(x)
    print("initial input var =", x)
    print("initial coefficient =", coefficient)
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    print("========================")
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        print("Debug1 : idx=", idx, ", x[idx]=", x[idx])
        x[idx] = tmp_val + deltaX
        print("Debug2 : x=", x)
        fx1 = f(x)
        print("Debug3 : fx1=", fx1)
        x[idx] = tmp_val - deltaX
        fx2 = f(x)  # f(x-deltaX)
        print("Debug4 : fx2=", fx2)
        coefficient[idx] = (fx1 - fx2) / (2*deltaX)
        print("Debug5 : coefficient=", coefficient)
        print("Debug6 : x[idx]=", x[idx])
        x[idx] = tmp_val
        print("Debug7 : x[idx]=", x[idx])
        it.iternext()
        print("========================")
    return coefficient


input = np.array([[1.0, 2.0], [3.0, 4.0]])  # 입력값
print(input)
result = numericalDerivative(func, input)
print(result)  # 4변함수 수치미분 결과
