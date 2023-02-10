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
-> 특징7 : "+" 이용해서 리스트들을 합칠 수 있음
-> 특징8 : len을 이용해서 요소들의 길이를 알 수 있음
-> 특징9 : 리스트를 추가할 때는 extend 메소드를 사용
-> 특징10 : 리스트를 비우고 싶을 때 clear 메소드 사용
-> 특징11 : 위치를 선택해서 추가할 때 insert 메소드 사용 단, 입력이 2개 필요, 1번 째는 위치, 2번 째는 값
-> 특징12 : 값을 이용해 위치를 알고 싶을 때, index 메소드 사용
-> 특징13 : 값이 몇 개 있는지 확인 할 때에는 count 메소드 사용
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

# a=[1]
# b=[2,3]
# c=["가","나"]
# print(a+b+c)

# a=[1,2,3]
# print(len(a))

# a=[1,2,3]
# b=["가","나"]
# a.extend(b)
# print(a)

# a=[1,2,3]
# a.clear()
# print(a)

# a=[1,2,3]
# a.insert(1,100)
# print(a)

# a=[1,2,3]
# print(a.index(2))
# print(a.index(3))

# b=["가","나","다","나"]
# print(b.index("나"))

# a=["가","나","다","나"]
# print(a.count("나"))

# for i in range(1,5):
#     print(i)

# a=[1,2,3,4]
# for i in a:
#     print(i)

# b=["서현","하율","유래"]
# for i in b:
#     print(i)

# # Q1
# l=[]
# for i in range(1,21):
#     if i%2!=0:
#         l.append(i)
# l.reverse()
# print(l)
# # Q2
# st=[]
# for i in range(50,101):
#     if i%3==0:
#         if i%4==0:
#             st.append(i)
# st.reverse()
# print(st)
# # Q3
# print(l[0]*st[-1])

# # Q4
# a=[]
# for i in range(1,21):
#     if i%3==0:
#         a.append(i)
# a.reverse()
# print(a)

# Q5
def 구구단(입력):
    국웃안=[]
    for i in range(1,10):
        국웃안.append(i*입력)
    print(국웃안)

구구단(3)
구구단(8)