year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')
print({year})
print('{year}')
print(f'{year}')
print("I ate {0} apples. so I was sick for {day} days.".format(10, day=3))
print("===============")
tt = f"{year}"
print(tt)
print("===============")


# 왼쪽 정렬
print("{0:<10}".format("hi"))

# 오른쪽 정렬
print("{0:>10}".format("hi"))

# 가운데 정렬
print("{0:^10}".format("hi"))

# 공백 채우기
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

# { 또는 } 문자 표현하기
print("{{ and }}".format())

# 소수점 표현하기
y = 3.42134234
te = "{0:0.4f}".format(y)
print("te : ",te)
print("{0:10.4f}".format(y))


yes_votes = 42_572_634
no_votes = 43_132_495
print(yes_votes)
percentage = yes_votes / (no_votes + yes_votes)
print(percentage)

print('{:-9} YES votes {:2.2%}'.format(yes_votes, percentage))
# help(str)

print("|{:10}|".format(10))
print("|{:10}|".format("10"))

for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

import math
print('the value of pi is approximately %5.3f.' % math.pi)
