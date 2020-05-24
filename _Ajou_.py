import random

with open("./hangman.txt") as f:
    answer = str(random.choice(f.readlines())).strip()

print(answer)
print("------------------")
chance = 5
check = ["_" for init in range(len(answer))]

while(True):
    wrong_count = 0
    user_expect = input("[행맨게임] 단어를 맞춰보세요 : ")
    for index, keyword in enumerate(answer):
        if(keyword in (answer and user_expect)):
            check[index] = keyword
        else:
            wrong_count += 1
            check[index] = "_"
    if wrong_count == 0:
        print("성공입니다!!!")
        break
    else:
        chance -= 1
        if chance == 0:
            print("아쉽습니다...")
            break
        print("{0}번 기회가 남았습니다 : {1}".format(chance, "".join(check)))

print("---프로그램 종료---")