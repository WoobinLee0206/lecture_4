class Cat:
    color = 'red'

    #생성자 메소드
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        print("우리 {}는 색깔이 {}이고 자주 야옹~ 야옹~ 거려요".format(self.name, self.color))

raon = Cat('라온', '똥')
nabi = Cat('나비', '검정')
raon.meow()
print(nabi.color)
nabi.meow()