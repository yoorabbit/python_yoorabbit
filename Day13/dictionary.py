'''
딕셔너리(dictionary)
    파이썬에서 사용하는 자료구조 중 하나
    key와 value 쌍으로 이루어뎌 있음
    중괄호를 이용함{}
    indexing 가능함 key 값을 이용해서
    indexing method 이용가능
'''
# height={'서현':160,
#         '하율':140,
#         '유래':153}
# print(height['유래'])
# print(height.get('서현'))
# print(height.values())
# height.update({'하율':165})
# print(height)
# height['하율']=130
# print(height)
# height.update({'선생님':180})
# print(height)
# height['아인']=170
# print(height)
# del height['선생님']
# print(height)
# del height['아인']
# print(height)
# print('선생님'in height)
# print('하율'in height)
for i in range(11):
    fruits={"오렌지":30,"바나나":20,"사과":50}
    fruit=input("과일상점 임미당! 어떤 과일을 원하시나여?>v< : ")
    if fruit in fruits:
        print(f"{fruit}는 {fruits[fruit]}개 잇어영>v<")
    else:print(f"죄송하지만 저희 상점에는 {fruit}이 없어요 ㅠ.ㅠ")