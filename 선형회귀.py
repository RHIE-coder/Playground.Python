import numpy as np

# 입력값과 정답값
x_data = np.array([1, 2, 3, 4, 5]).reshape(5, 1)
t_data = np.array([5, 8, 11, 14, 17]).reshape(5, 1)

# W, b의 초기값 생성 H(x)
W = np.random.rand(1, 1)
b = np.random.rand(1)


# 손실함수 구현
def loss_func(x, t):
    y = np.dot(x, W) + b
    return np.sum(((t - y) ** 2)) / len(x)


# 수치미분 함수
def numericalDerivative(f, x):
    deltaX = 1e-4
    coefficient = np.zeros_like(x)
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])

    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]

        x[idx] = tmp_val + deltaX
        fx1 = f(x)

        x[idx] = tmp_val - deltaX
        fx2 = f(x)

        coefficient[idx] = (fx1 - fx2) / (2*deltaX)

        x[idx] = tmp_val
        it.iternext()

    return coefficient


# 학습시키기
Epoch = 10000  # 반복할 학습 횟수
learning_rate = 1e-2  # 학습률 지정 : 1e-2, 1e-3, 1e-4, 1e-5, 1e-6 많이 사용


def f(x):
    return loss_func(x_data, t_data)  # 정답값과 얼마나 떨어졌는지 확인


for i in range(Epoch):
    # 수치미분을 통한 W, b값 갱신
    W -= learning_rate * numericalDerivative(f, W)
    b -= learning_rate * numericalDerivative(f, b)

    if i % 1000 == 0:
        print("오차범위:{}[{}번째]".format(loss_func(x_data, t_data), i))


# 학습을 마친 후, 예측하기
print("학습결과(W,b):({},{})".format(W, b))
print('='*50)
x = int(input("임의의 숫자를 입력하세요 (example:50) : "))
y = np.dot(x, W)+b
print(y)
