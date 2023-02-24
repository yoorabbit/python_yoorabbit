'''
범위지정(slice)
ㄴ A:B
A이상 B미만

생략 가는한 slice
   처음부터 시작할 때 "0" 생략 가능
   맨 마지막 생략 가능
'''
# a=[]
# for i in range(1,11):
#     a.append(i)
# print(a)
# print(a[1:4])
# print(a.index(2))
# # print(a[a.index(2):a.index(5)])
# print(a[0:4])
# print(a[:4])
# print(a[8:10])
# print(a[8:])

# b=["watermelon","banana","cherry","apple"]
# print(b[:1]+b[2:])
# b.sort()
# print(b[1:3])
# b.append("orange")
# b.reverse()
# print(b[:3])

# c=[]
# for i in range(1,21):
#     if i%2==0:
#         c.append(i)
# print(c[4:])
# print(c[:4])
# print(c[2:7])

# 하율생일=[1,1,1,0,1,7]
# 유래생일=[1,1,0,5,0,2]
# 서현생일=[1,1,0,1,1,6]
# print(하율생일[2:4])
# print(유래생일[2:4])
# print(서현생일[2:4])
# print(하율생일[4:])
# print(유래생일[4:])
# print(서현생일[4:])
# print(하율생일[:2])
# print(유래생일[:2])
# print(서현생일[:2])

d=[]
for i in range(1,31):
    if i%7==0:
        d.append(i)
print(d[:])
print(d[:2])