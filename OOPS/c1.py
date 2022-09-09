class Cat:
    breed=None
    gender=None
    fur_color=None
    age=None
    weight=None
    Height=None
    is_tamed=None

    def eat(self, food='catfood'):
        print(f'🐈 is eating{food}')
    def play(self):
        print('🐈 is playing') 
    def sleep(self):
        print('🐈is sleeping')

billu=Cat() # constructor calling
tom=Cat()
Bagadbilla=Cat()

billu.breed='persian'
billu.weight=2
billu.age=2
billu.fur_color='white'
billu.Height=1
billu.is_tamed=True
billu.gender='M'

tom.breed='Street Cat'
tom.weight=1.5
tom.age=100
tom.fur_color='grey'
tom.Height=1.1
tom.is_tamed=True
tom.gender='M'

Bagadbilla.breed='Wild cat'
Bagadbilla.weight=2.5
Bagadbilla.age=5
Bagadbilla.fur_color='Brown'
Bagadbilla.Height=2
Bagadbilla.is_tamed=False
Bagadbilla.gender='M'

print('billu details')
print('breed',billu.breed)
print('gender',billu.gender)
print('age',billu.age)
print('weight',billu.weight)
print('Height',billu.Height)
print('fur_color',billu.fur_color)
print('pet:','yes' if billu.is_tamed else 'no')
billu.sleep()
billu.play()
billu.sleep()

print('tom details')
print('breed',tom.breed)
print('gender',tom.gender)
print('age',tom.age)
print('weight',tom.weight)
print('Height',tom.Height)
print('fur_color',tom.fur_color)
print('pet:','yes' if tom.is_tamed else 'no')
tom.eat()
tom.play()
tom.sleep()

print('bagadbilla details')
print('breed',Bagadbilla.breed)
print('gender',Bagadbilla.gender)
print('age',Bagadbilla.age)
print('weight',Bagadbilla.weight)
print('Height',Bagadbilla.Height)
print('fur_color',Bagadbilla.fur_color)
print('pet:','yes' if Bagadbilla.is_tamed else 'no')
Bagadbilla.eat()
Bagadbilla.eat()
Bagadbilla.sleep()
