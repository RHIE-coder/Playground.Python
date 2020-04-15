x = 10

if x < 0:
    print("negetive")
elif x < 5:
    print("under 5")
elif x < 10:
    print("under 10")
else:
    print("finally :", x)


nums = [1,2,3,4,5]
for i in nums:
    print("for문 : ",i)

for i in range(5,22,3):
    print(i)

testli =[
    ["a",1],["b",2],["c",3]
]

print(testli)

for i,j in testli:
    print("i, j = ", i, j)

print(range(5)) #range는 iterator임
print(list(range(5)))

# continue와 break

# pass 문은 아무것도 하지 않습니다. 문법적으로 문장이 필요하지만, 프로그램이 특별히 할 일이 없을 때 사용할 수 있습니다.
# ...특히 최소한의 클래스를 만들 때 흔히 사용됨
def initlog(*args):
    pass   # Remember to impklement this!

def myFunc(n):
    print("myFunc")
    print(n)
myFunc(10)

copyFunc = myFunc
print(copyFunc)