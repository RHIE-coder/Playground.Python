""" tuple """

t = 1234, 4567, "hello"
print(t)

n = t, (1,23,4)
print(n)

# and tuple is immutable

v = ([1,2,3],[4,5,6])
v[0][1] = 10 # list is mutable
print(v)

x,y,z = t
print(x, y, z)

""" set """

basket = {1,2,3,4,5,6}
2 in basket
[i for i in basket]
a = set("abracadabra")
b = set("alacazam")
print(a)
print(b)
a - b
a | b
a & b
a ^ b # letters in a or b but not both
aa = {x for x in 'abracadabra' if x not in 'abc'}
print(aa)

bb = set() # empty set
bb.add("a")
bb.add("b")
bb.add("c")
bb

cc = {"a"}
print(bb & cc)


""" dictionary """
d = {} # empty dictionary
# del 키워드로 키:값 쌍을 삭제하는 것도 가능

d = {"E" : 0, "A" : 10, "B" : 20, "C" : 30}
d["D"] = 40
print(d)

del d["C"]
print(d)
print(list(d))
print(sorted(d))

print(dict([('scape',4123),('guido',4234),('jack',2402)]))
print({x: x**2 for x in (2, 4, 6)})
x = dict(scape=1232,guido=4234,jack=3249)
print(x)
print(x.items())

for k, v in x.items():
    print(k, v)

for i, v in enumerate(['tic','tac','toe']):
    print(i, v)

questions = "name", "quest", "favorite color"
answers = "lancelot", "the holy grail", "blue"
print(questions)
print(answers)
for q, a in zip(questions, answers):
    print("What is your {0}? It is {1}.".format(q,a))

for i in reversed(range(1,10,2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# 루프를 돌고 있는 리스트를 변경하고픈 유혹을 느낍니다. 하지만, 종종, 대신 새 리스트를 만드는 것이 더 간단하고 더 안전합니다.
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in reversed(sorted(set(raw_data))):
    if not math.isnan(value):
        filtered_data.append(value)
    
print(filtered_data)