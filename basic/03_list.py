kor = ["사과", "바나나", "포도", "토마토", "오렌지", "수박"]
eng = ["apple", "banana", "grape", "tomato", "orange", "watermelon"]
score = 0
answer = ""

for i in range(len(kor)):
    answer = input(f"{kor[i]}을/를 영어로 하면? : ")
    if answer == eng[i]:
        score = score + 1
        print("맞음")
    else:
        print("틀림")
print(f"점수 : {score} 점")

# running = True
# count = 0

# while running:
#     answer = input(f"{kor[count]}을/를 영어로 하면? : ")
#     if answer == eng[count]:
#         score = score + 1
#         print("맞음")
#     else:
#         print("틀림")
#     count += 1
#     if count >= len(kor):
#         running = False
# print(f"점수 : {score} 점")