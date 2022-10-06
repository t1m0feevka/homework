class Animals:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, 'eats like an animals')

    def sleep(self):
        print(self.name, 'sleeps like an animal')


class Tiger(Animals):
    def hunt(self):
        print(self.name, 'hunts')


class Zebra(Animals):
    def run(self):
        print(self.name, 'runs')


class Lion(Animals):
    def growls(self):
        print(self.name, 'ARRRRRRRRRRRRRRRRRRRRR')


class Giraffe(Animals):
    def eat(self):
        print(self.name, 'eat trees')


class Mammoth(Animals):
    def die_out(self):
        print(self.name, 'die out')


Animal1 = Tiger('Tiger Diego')
Animal2 = Zebra('Zebra Marti')
Animal3 = Lion('Lion Alex')
Animal4 = Giraffe('Giraffe Melman')
Animal5 = Mammoth('Mammoth Manfred')

Animal1.hunt()
Animal2.run()
Animal1.eat()
Animal2.sleep()
Animal3.growls()
Animal4.eat()
Animal5.die_out()

print(isinstance(Animal1, Animals))
print(isinstance(Animal2, Animals))
print(isinstance(Animal3, Animals))
print(isinstance(Animal4, Animals))
print(isinstance(Animal5, Animals))
