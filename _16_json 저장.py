import json
r = json.dumps([1,'simple','list'])
print(r)
print(type(r))

"""  
dump()라는 dumps() 함수의 변종은 객체를 텍스트 파일로 직렬화합니다. 그래서 f 가 쓰기를 위해 열린
텍스트 파일 이면, 이렇게 할 수 있습니다:

    json.dump(x, f)

객체를 다시 디코드하려면, f 가 읽기를 위해 열린 텍스트 파일 객체일 때:

    x = json.load(f)

"""
"=========================직렬화 과정================================="
student_data = {
    "1.FirstName": "Gildong",
    "2.LastName": "Hong",
    "3.Age": 20, 
    "4.University": "Yonsei University",
    "5.Courses": [
        {
            "Major": "Statistics", 
            "Classes": ["Probability", 
                        "Generalized Linear Model", 
                        "Categorical Data Analysis"]
        }, 
        {
            "Minor": "ComputerScience", 
            "Classes": ["Data Structure", 
                        "Programming", 
                        "Algorithms"]
        }
    ]
} 

print(json.dumps(student_data, indent=4)) # return json string
sss = json.dumps(student_data, indent=4)

with open("jsonFileSample.json","r+") as json_file:
    print(json.dump(student_data, json_file)) #None


print("=========================역직렬화 과정=================================")


print(json.loads(sss))

with open("jsonFileSample.json","r") as st_json:
    st_python = json.load(st_json)
    print(st_python)


""" https://rfriend.tistory.com/474 """

print("\n\n\n\n\n\n")
a = json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
print(type(a))
print(a)