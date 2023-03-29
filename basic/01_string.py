name = ""
gender = ""
age = 0

# print (name,len(name), age - 10)
name = input("이름을 넣거라 : ")
gender = input("너의 성별은(남/여) : ")
age = input("나이를 넣어랏 : ")

if gender == "남":
    gender = "Mr."
elif gender == "여":
    gender = "Ms."
print(f"Welcome {gender}{name[0]}. This is your 'MAGAM' Hell!")

if int(age) <= 18:
    print("이히히 미성년자야? 그럼 이제 학생이라는 죄로 학교라는 교도소에서 교실이라는 감옥이 갇혀 출석부라는 죄수명단에 올라 교복이란 죄수복을 입고 공부란 벌을 받고 졸업이란 석방을 기다리세요!")
elif int(age) >= 19:
    print("어서오세요! 마감지옥에!!")