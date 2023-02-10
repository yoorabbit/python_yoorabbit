'''
막대그래프 그리기
-모듈설치 필요함
-Python 모듈을 설치할 때는 pip 명령어를 쓴다
-터미널 창에서 "pip install matplotlib" 를 입력
'''
import matplotlib.pyplot as plt
fruits=["apple","blueberry","cherry","orange"]
counts=[5,10,7,12]
bar_color=["black","black","black","black"]
창,내용=plt.subplots(1,3)
내용[0].bar(fruits,counts,color=bar_color)
내용[1].barh(fruits,counts,color=bar_color)
내용[2].bar(fruits,counts,color=bar_color)
plt.show()