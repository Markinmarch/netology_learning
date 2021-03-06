# ***НАСЛЕДОВАНИЕ ДОЧЕРНЕЕ***

class Charecter:
    name = ''
    power = 0
    energy = 100
    hands = 2

class Spider:
    power = 0
    energy = 50
    hands = 8

    def webshoot(self):
        print('Pew-pew!')

class SpiderMan (Charecter, Spider):
    pass

peter_parker = SpiderMan()
print(peter_parker.name)
print(peter_parker.power)
print(peter_parker.energy)
print(peter_parker.hands)
peter_parker.webshoot()

print(SpiderMan.mro())



class Charecter:
# переносим всё в init
    def __init__(self, name, power, energy = 100, hands = 2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands

    def webshoot(self):
        print('Pew-pew!')

class SpiderMan (Charecter, Spider):
    pass

    def turn_spider_sense(self):
        self.energy -= 10
        self.power += 20

peter_parker = SpiderMan('Peter Parker', 80)

print(peter_parker.name)
print(peter_parker.power)
print(peter_parker.energy)
print(peter_parker.hands)
peter_parker.turn_spider_sense()
print(peter_parker.power)
print(peter_parker.energy)

print(SpiderMan.mro())



# ***ПОЛИМОРФИЗМ*** 
# Позволяет методам с одинаковыми именами реализовать разную функциональность для разных классов (в т.ч. дочерних)

class Charecter:
    def __init__(self, name, power, energy = 100, hands = 2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

# ***функция move в обеих классах реализует полиморфизм
    def move(self):
        print('Двигайтесь на 2 клетки')

class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands

    def webshoot(self):
        print('Pew-pew!')

# ***функция move в обеих классах реализует полиморфизм
    def move(self):
        self.webshoot()
        print('Двигайтесь на 1 клетку')

class SpiderMan (Charecter, Spider):
    def turn_spider_sense(self):
        self.energy -= 10
        self.power += 20

# ***функция move в обеих классах реализует полиморфизм
    def move(self):
        self.webshoot()
        print('Двигайтесь на 3 клетки')

peter_parker = SpiderMan('Peter Parker', 80)
peter_parker.move()



class Charecter:
    # переносим всё в init
    def __init__(self, name, power, energy = 100, hands = 2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands

    # ***функция move в обеих классах реализует полиморфизм
    def move(self):
        print('Двигайтесь на 2 клетки')

class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands

    def webshoot(self):
        print('Pew-pew!')

    # ***функция move в обеих классах реализует полиморфизм
    def move(self):
        self.webshoot()
        print('Двигайтесь на 1 клетку')

class SpiderMan (Charecter, Spider):

# функция super() позволяет получить доступ к унаследованным методам, которые 
# были перезаписаны в дочернем классе
    def __init__(self, name, power):
        super().__init__(name, power)
        self.backpack = []

    def turn_spider_sense(self):
        self.energy -= 10
        self.power += 20

    # ***функция move в обеих классах реализует полиморфизм
    def move(self):
        self.webshoot()
        print('Двигайтесь на 3 клетки')

    def webshoot(self):
        if 'web' in self.backpack:
# здесь тоже наследование 
            super().webshoot()
        else:
            print('Нет паутины!')

peter_parker = SpiderMan('Peter Parker', 80)
print(peter_parker.backpack)
print(peter_parker.power)
print(peter_parker.energy)
print(peter_parker.hands)
peter_parker.webshoot()
peter_parker.backpack.append('web')
peter_parker.webshoot()