class Cat:
    def __init__(self , name , color="흰색"):
        self.name = name
        self.color = color

    def meow(self, name):
        print('내이름은 {}, 색깔은 {}, 양옹양옹'.format(self.name, self.color)) #self.a, self.b 써도 무방
        print('속도는', name)
nabi = Cat('나비')
nabi.meow(100)

nero = Cat('네로','검은색')
nero.meow(40)

mimi = Cat('미미','갈색')
mimi.meow(30)