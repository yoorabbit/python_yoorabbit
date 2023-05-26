'''
클래스(class)
2.상속(inheritance)
클래스의 기능을 물려받는 것
-부모클래스(parent class), 자식클래스(child class)
문법) class 자식클래스이름(부모클래스):
            xxx
3.오버라이딩(overriding)
-상속받은 부모클래스릐 기능을 재정의 하는 것
'''
class 연산:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def 더하기(self):
        return self.a+self.b
    def 빼기(self):
        return self.a-self.b
    def 곱하기(self):
        return self.a*self.b
    def 나누기(self):
        return self.a/self.b
class 추가연산(연산):
    def 제곱(self):
        return self.a**self.b
    def 빼기(self):
        if self.a>self.b:
            return self.a-self.b
        else:
            return self.b-self.a
    def 나누기(self):
        if self.b==0:
            return -999
        else:
            return self.a/self.b
사칙연산=연산(1,2)
# print(사칙연산.더하기())
# print(사칙연산.빼기())
# print(사칙연산.곱하기())
# print(사칙연산.나누기())
자식사칙연산=추가연산(4,0)
# print(자식사칙연산.더하기())
# print(자식사칙연산.빼기())
# print(자식사칙연산.곱하기())
print(자식사칙연산.나누기())
# print(자식사칙연산.제곱())