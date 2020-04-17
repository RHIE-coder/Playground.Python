'''
1. REPL 이란
콘솔 화면에서 파이썬 구문을 입력하면 바로 결과를 반환하고 다시 입력할수 있는 도구.
Read Evaluate Print Loop의 줄임말

    _ 는 바로 직전 결과 값을 나타냄
'''

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple')) # 리스트에서 x 가 등장하는 횟수를 돌려줍니다.
print(fruits.index('banana')) # index 반환
re = fruits.index('banana', fruits.index('banana')+1)
print(re)
print(type(fruits))

re2 = fruits.pop()
print(type(re2))
print(re2)
print(fruits)

""" 
list.append(x)
    리스트의 끝에 항목을 더합니다. 
    a[len(a):] = [x] 와 동등합니다.

list.extend(iterable)
    리스트의 끝에 이터러블의 모든 항목을 덧붙여서 확장합니다. 
    a[len(a):] = iterable 와 동등합니다.

list.insert(i, x)
주어진 위치에 항목을 삽입합니다. 첫 번째 인자는 삽입되는 요소가 갖게 될 인덱스입니다. 그래서 a.insert(0, x) 는 리스트의 처음에 삽입하고, a.insert(len(a), x) 는 a.append(x) 와 동등합니다.

list.remove(x)
리스트에서 값이 x 와 같은 첫 번째 항목을 삭제합니다. 그런 항목이 없으면 ValueError를 일으킵니다.

list.pop([i])
리스트에서 주어진 위치에 있는 항목을 삭제하고, 그 항목을 돌려줍니다. 인덱스를 지정하지 않으면, a.pop() 은 리스트의 마지막 항목을 삭제하고 돌려줍니다. (메서드 시그니처에서 i 를 둘러싼 대괄호는 매개변수가 선택적임을 나타냅니다. 그 위치에 대괄호를 입력해야 한다는 뜻이 아닙니다. 이 표기법은 파이썬 라이브러리 레퍼런스에서 지주 등장합니다.)

list.clear()
리스트의 모든 항목을 삭제합니다. del a[:] 와 동등합니다.

list.index(x[, start[, end]])
리스트에 있는 항목 중 값이 x 와 같은 첫 번째 것의 0부터 시작하는 인덱스를 돌려줍니다. 그런 항목이 없으면 ValueError 를 일으킵니다.

선택적인 인자 start 와 end 는 슬라이스 표기법처럼 해석되고, 검색을 리스트의 특별한 서브 시퀀스로 제한하는 데 사용됩니다. 돌려주는 인덱스는 start 인자가 아니라 전체 시퀀스의 시작을 기준으로 합니다.

list.count(x)
리스트에서 x 가 등장하는 횟수를 돌려줍니다.

list.sort(key=None, reverse=False)
리스트의 항목들을 제자리에서 정렬합니다 (인자들은 정렬 커스터마이제이션에 사용될 수 있습니다. 설명은 sorted() 를 보세요).

list.reverse()
리스트의 요소들을 제자리에서 뒤집습니다.

list.copy()
리스트의 얕은 사본을 돌려줍니다. a[:] 와 동등합니다.
"""
a = [1,2,3,1,2,1,2,3,1]
a[len(a):] = [10] # append
print(a)

a.insert(2,100)
print(a)
a.remove(1) # 값으로 삭제
print(a)
a.pop() 
a.pop(0) # index로 삭제
print(a)
print(a.index(1, 7, len(a)))
a.extend([10,20,30])
print(a)

# 리스트로 스텍 활용은 괜찮은데 queue로 활용하면 느림
# ...모두 한칸식 이동해야하기 때문임
from collections import deque
queue = deque(["Eric","John","Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
queue.popleft()
print(queue)
print(type(dir(queue)))
print(dir(queue))

squares = []
# 구 방식
# for x in range(10):
#     squares.append(x ** 2)

# !?
def anony(x):
    return x ** 2
m = map(anony,range(10))
print(tuple(m))

# !!! 향상된 방식
good = list(map(lambda x : x ** 2, range(10)))
print("good : ", good)

# 신 방식
squares = [x**2 for x in range(10)]
print(squares)

# wow...
wow = [(x, y) for x in [1,2,3] for y in [3,1,4] if x is not y]
print(wow)

# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x,y))

vec = [[1,2,3],[4,5,6],[7,8,9]]
print([num for elem in vec for num in elem])
#print([num for num in elem for elem in vec]) error

# 중첩된 리스트 컴프리헨션
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

result = [row[i] for row in matrix for i in range(4)]
result2 = []

print(result)

# transposed=[]
# for i in range(4):
#     transposed_row = []
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)

# dictionary의 map 활용
dic = {
    1 : 10,
    5 : 30,
    9 : 50
}

def testFunc(x):
    return x * 2

print(list(map(testFunc, dic)))
print(list(dic[i] for i in dic ))
print(lambda y : y * 10, [y for y in dic])
print(map(lambda y : y * 10, [y for y in dic]))
print(list(map(lambda y : y * 10, [y for y in dic])))

result = list([row[i] for row in matrix] for i in range(4))
print(result)

# zip : 김밥을 만들어서 칼로 자르는 느낌
print("===============")
print(list(zip(*matrix)))

