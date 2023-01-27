'''
리스트(aka.array)
-> 데이터를 저장하는 방식 중 하나
-> 규칙은 대괄호와 쉼표로 구분
-> 출력 시 모두 나타남
-> 특징1 : 순서로 안에있는 내용을 선택할 수 있음(indexing)
    :순서는 0부터 시작(항상)
    :선택할때도 대괄호 사용함
    :마지막 순서는 -1 해도 무방
-> 특징2 : append 를 이용해 추가할 수 있음(메소드 이용)
-> 특징3 : pop을 이용해 삭제할 수 있음
        * 맨 마지막 게 사라짐
-> 특징4 : 선택한 값을 지우고 싶을땐 remove 사용
-> 특징5 : 정렬(오름차순) 할때 sort 사용
-> 특징6 : 정렬(내림차순) 할때 reverse 사용
'''
# a=10
# b="하율"
# c=["사과","배","바나나"]
# d=[10,20,30]
# e=["축구",2,"아구",3]
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(d[0]+d[1])
# print(d[2]//d[0])
# print(d[-1]-d[1])

# 요일=["일요일","월요일"]
# print(요일)
# 요일.append("화요일")
# print(요일)
# 요일.pop()
# print(요일)
# 요일.remove("일요일")
# print(요일)

# fruit=["orange","watermelon","banana","apple"]
# fruit.sort()
# print(fruit)
# fruit.reverse()
# print(fruit)

# l=[]
# for i in range(10,21):
#     if i%3==0:
#         l.append(i)
# l.reverse()
# print(l)

# Q1
l=[]
for i in range(1,21):
    if i%2!=0:
        l.append(i)
l.reverse()
print(l)
# Q2
st=[]
for i in range(50,101):
    if i%3==0:
        if i%4==0:
            st.append(i)
st.reverse()
print(st)
# Q3
print(l[0]*st[-1])