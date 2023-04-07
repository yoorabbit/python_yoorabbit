'''
f-string사용법
-python표현방식 중 하나
(문법)f" "
ㄴ>변수는 { }중괄호 안에

입력(input)<->출력(print)
'''
# str="오늘은 금요일"
# print(str)
# fstr=f"내일은 토요일"
# print(fstr)
# age=19
# name="뉴진스"
# fstr2=f"내 나이는 {age}이고, 이름은 {name}입니다"
# print(fstr2)
# ani="고양이"
# stu="초등학생"
# fstr3=f"나는 {ani}를 좋아하는 {stu}입니다"
# print(fstr3)
# for i in range(3):
#     입력한거=input("나이를 입력하세여><:")
#     print(f"당신의 나이는 {입력한거}이군여!><")
# for i in range(3):
#     gender=input("성별을 알려주세여><(남/여):")
#     name=input("이름을 알려주세여><:")
#     print(f"당신은 {gender}자이고 이름은 {name}이네여! 반가워여!><")
for i in range(5):
    num1=input("첫 번째 숫자를 넣어주세여><:")
    num2=input("두 번째 술자를 넣어주세여><:")
    print(f"두 수의 합은 {int(num1)+int(num2)}임미다><")