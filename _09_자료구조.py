# tuple
t = 1234,5678,"hi"
print(t)
t2 = "h""e""l""l""o"
t2 = "h""e""l""l""o",str(1) # 튜플로 만들어짐
t2 = "h""e""l""l""o"+str(1) # 합쳐져서 문자열로 만들어짐
print(t2)
l = ["1",2,3.0]
print(l)

t3 = 'world'
print(t3)
print(len(t3))
t4 = 'world', # <-- note trailing comma
print(t4)
print(len(t4))

x,y,z = t

(lambda x : print(x))(111)

source = [12, 16, 24, 5, 20, 27, 12, 8, 9, 110, 51, 26, 13, 21, 40, 63, 76, 64, 78]

# print(list(s[i] for s in source for i in range(len(source)) if source[i]<=60 and source[i]<=100 and source[i] % 2 is 0 ))
print(list(s for s in source if s % 2 == 0 and 60 <= s and s <= 100))

testList = [i+1 for i in range(50)]
print(testList) # [ 1,2,3,...,47,48,49,50]
print([(a, b) for a in testList for b in testList if a is 2 and b % 2 is 1])

dic = {
    1 : 10,
    5 : 30,
    9 : 50
}

print([a for a in dic])
print([dic[i] for i in dic])

# 행렬 곱하기 
matrA = [[1,2],[3,4]]
matrB = [[2,3],[4,5]]

b = [[row[i] for row in matrB] for i in range(2)]
print(list([matrA[i][0] * b[j][0] + matrA[i][1] * b[j][1] for j in range(2)] for i in range(2)))


result = []
for i in range(2):
    tmp = []
    for j in range(2):
        tmp.append(matrA[i][0] * b[j][0] + matrA[i][1] * b[j][1])
    result.append(tmp)
print(result)




testMatr=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

# print([[elem[i] for elem in testMatr] for i in range(4)])
