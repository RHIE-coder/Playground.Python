import sys
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)
# 논리 연산자(and, or)는 단락-회로(short-circuit) 연산자입니다. 인자들은 오른쪽으로 값이 구해지고
# ... 결과가 결정되자마자 값 구하기는 중단 됩니다.
a, b ,c = True, False, True
print(a and b and c)
print(a and b or c)
print(string2 or string3)

print((1,1,1) > (1,))
