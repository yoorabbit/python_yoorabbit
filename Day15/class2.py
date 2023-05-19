'''
클래스(class)
1.생성자(constructor)
;객체를 생설할 때 자동으로 호출되는 method
문법 class 이름:
    def__init__(self):
        작성
'''
# class 수학:
#     def 더하기(self,a,b):
#         결과=a+b
#         return 결과
# 초등수학=수학()
# print(초등수학.더하기(10,20))
class 강아지:
    def __init__(self,강아지눈,강아지털,강아지이름):
        self.강아지눈=강아지눈
        self.강아지털=강아지털
        self.강아지이름=강아지이름
    def 소개하기(self):
        print(f"강아지 눈은{self.강아지눈}개이고, 강아지 털은 {self.강아지털}이며, 강아지 이름은 {self.강아지이름}임미당>v<")
우리집강아지=강아지(2,"검은색","검둥이")
print(우리집강아지.강아지눈)
print(우리집강아지.강아지털)
print(우리집강아지.강아지이름)
친구집강아지=강아지(2,"무지개색","댕댕이")
print(친구집강아지.강아지눈)
print(친구집강아지.강아지털)
print(친구집강아지.강아지이름)
하율이네강아지=강아지(3,"사람색","이승욱")
하율이네강아지.소개하기()

# 문제
class 연산:
    def __init__(self, 첫번째수, 두번째수):
        self.첫번째수=첫번째수
        self.두번째수=두번째수
    def 더하기(self):
        결과=self.첫번째수+self.두번째수
        return 결과
    def 빼기(self):
        결과=self.첫번째수-self.두번째수
        return 결과
    def 곱하기(self):
        결과=self.첫번째수*self.두번째수
        return 결과
    def 나누기(self):
        결과=self.첫번째수/self.두번째수
        return 결과
사칙연산=연산(3,5)
print(사칙연산.더하기())
print(사칙연산.빼기())
print(사칙연산.곱하기())
print(사칙연산.나누기())