class Bird():
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color
    def fly(self):
        print(f"{self.name} летает")
    def eat(self):
        print(f"{self.name} ест")
    def sing(self):
        print(f"{self.name} поет - чирик")
    def info(self):
        print(f"{self.name}   - имя")
        print(f"{self.voice}  - голос")
        print(f"{self.color}  - окрас птицы")

class Pigeon(Bird):
    def __init__(self, name, voice, color, favorite_food):
        super().__init__(name, voice, color)
        self.favorite_food = favorite_food
    def walk(self):
        print(f"{self.name} гуляет")
    def sing(self):
        print(f"{self.name} поет - курлык курлык")


bird1 = Pigeon("гоша", "курлык", "белый", "хлебные крошки")

bird2 = Bird("Маша", "чирик", "серый")
bird1.sing()
bird1.info()
bird1.walk()