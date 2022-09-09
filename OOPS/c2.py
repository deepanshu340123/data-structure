from turtle import window_height


class Cat:

    def __init__(self, breed,fur_color,gender='F',age=1,w=1,h=1,is_tamed=True):
        self.breed=breed
        self.fur_color=fur_color
        self.gender=gender
        self.age=age
        self.weight=w
        self.height=h
        self.is_tamed=is_tamed

    def eat(self, food='catfood'):
        print(f'🐈 is eating{food}')
    def play(self):
        print('🐈 is playing') 
    def sleep(self):
        print('🐈is sleeping')    
    def info(self):
        print('🐈🐈'*15) # optional design
        print(f'breed: {self.breed}')
        print(f'Age: {self.age}year')
        print(f'weight: {self.weight}kg')
        print(f'height: {self.height}ft')
        print(f'gender: {self.gender}')
        print(f'is_tamed: {self.is_tamed}')
        print(f'fur_color: {self.fur_color}')
        print('🐈🐈'*15) #optional design


tom=Cat('street cat','grey',age=100,gender='M')
soni=Cat('House cat','brown',age=3) 
snowbell=Cat('persian','white',age=5)

print('TOM')
tom.info()
tom.eat('jerry')

print('SNOWBELL')
snowbell.info()
snowbell.eat('stuart')


