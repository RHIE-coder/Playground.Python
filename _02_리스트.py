li = [1,24,9,16]
li2 = li[:]
print(li)

li2[1] = 10
print(li)

# + 로 이어붙일 수 있음
# 중첩도 가능

a,b = 0,1
while a < 10:
    print(a)
    a,b = b, a+b