a = "This is Anfield, This is Anfield, This is Anfield"
b = "This is Anfield, This is Anfield, This is Anfield"
print(id(a))
print(id(b))
print(a is b)

strA = "AAA"
strB = "BBB"
strC = "CCC"
print(id(strA))
print(id(strB))
print(id(strC))
result = strA + strB + strC
print(id(result))




while(True):
    a = input("String : ")
    print(id(a))
    print("int({0}) : ".format(id(int(a))))
    print("1 : ", id(1))
    print("2 : ", id(2))
    print("3 : ", id(3))
    print("4 : ", id(4))
    print("5 : ", id(5))
    print("6 : ", id(6))
    print("7 : ", id(7))
    print("8 : ", id(8))
    print("9 : ", id(9))
    if(a == "1111"):
        break

def test():
    a = 695124378921749142132142134213521342142142154214321521421421521421321421421421321
    print(id(a))
    print(id(695124378921749142132142134213521342142142154214321521421421521421321421421421321))
    print(a is 695124378921749142132142134213521342142142154214321521421421521421321421421421321)

test()