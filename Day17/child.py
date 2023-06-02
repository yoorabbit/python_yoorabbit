import parent as p
class Female(p.Person):
    def greeting(self):
        print(f"Hello,everyone^^")
class male(p.Person):
    def greeting(self):
        print(f"Hi, guys T.T")
class pencil(p.상품):
    def how_much_dozen(self):
        print(f"{self.name}의 한 다스 가격은 {self.price*12}원 입니다")
class eraser(p.상품):
    def how_much_pack(self):
        print(f"{self.name}의 한 팩 가격은 {self.price*10}원 입니다")