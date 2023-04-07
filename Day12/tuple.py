'''
튜플(tuple)
(문법)
[ ](x)
( )(o)
immutable 특징
(변경 불가능한)
indexing 가능->[ ](읽기 가능)
list메소드 사용x
리스트(list)
[ ]
mutable 특징(쓰기 가능)
(변경 가능한)
indexing->[ ](읽기 가능)
slicing->c
'''
a=[1,2,3]
b=(1,2,3)
a[2]=100
# b[2]=100
c=tuple(a)
print(a)
print(b)
print(b[0])
print(a[:2])
print(b[:2])
print(c)