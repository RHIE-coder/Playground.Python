import numpy as np

# 학습데이터 생성
x1_data = np.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]).reshape(10, 1)
x2_data = np.array([4, 11, 6, 5, 7, 16, 8, 3, 7, 9]).reshape(10, 1)
t_data = np.array([0, 0, 0, 0,  1,  1,  1,  1,  1, 1]).reshape(10, 1)


# 초기값 생성
W = np.random.rand(1, 1)
b = np.random.rand(1)


# 시그모이드 함수 구현
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# 손실함수 구현
def loss_func(x, t):
    delta = 1e-7
    z = np.dot(x, W) + b
    y = sigmoid(z)
    return -np.sum(t*np.log(y + delta) + (1 - t)*np.log((1 - y) + delta))


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


# x1과 x2를 따로 학습시키기
Epoch = 10001  # 반복할 학습 횟수
learning_rate = 1e-2  # 학습률 지정 : 1e-2, 1e-3, 1e-4, 1e-5, 1e-6 많이 사용


def f1(x):
    return loss_func(x1_data, t_data)


def f2(x):
    return loss_func(x2_data, t_data)


print("x1_data에 대한 학습 시작")
for i in range(Epoch):

    # 수치미분을 통한 W, b값 갱신
    W -= learning_rate * numericalDerivative(f1, W)
    b -= learning_rate * numericalDerivative(f1, b)

    if i % 1000 == 0:
        print("오차범위:{}[{}번째]".format(loss_func(x1_data, t_data), i))

# x1_data에 대한 결과 저장
W1, b1 = W, b

# 초기값 생성
W = np.random.rand(1, 1)
b = np.random.rand(1)


print("x2_data에 대한 학습 시작")
for i in range(Epoch):
    # 수치미분을 통한 W, b값 갱신
    W -= learning_rate * numericalDerivative(f2, W)
    b -= learning_rate * numericalDerivative(f2, b)

    if i % 1000 == 0:
        print("오차범위:{}[{}번째]".format(loss_func(x2_data, t_data), i))

# x2_data에 대한 결과 저장
W2, b2 = W, b


def predict(x):
    z = np.dot(x, W) + b
    y = sigmoid(z)
    if y > 0.5:
        result = 1
    else:
        result = 0
    return y, result


# 학습을 마친 후, 예측하기
print("학습결과(W,b):({},{})".format(W, b))
print('='*50)

userInput = input("임의의 2개의 숫자를 입력하세요 (example:'12,0') : ")
result = userInput.split(",")

W, b = W1, b1
x1 = predict(int(result[0]))

W, b = W2, b2
x2 = predict(int(result[1]))
print("첫번째의 예측값 :", x1)
print("두번째의 예측값 :", x2)
