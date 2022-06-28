
class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.sound = self.getSound()

    def getSound(self):
        if self.type == 'Cat':
            return 'Meow'
        else:
            return 'Bark'

def getAandB(a, b):
    newA = a + 5
    newB = b + 5

    return newA, newB


def addAandB(a, b):
    c = a + b
    return c


def Main():
    a, b = getAandB(1, 2)
    c = addAandB(a, b)
    print(c)

    Animal1 = Animal('Norah', 'Cat')
    Animal2 = Animal('Samson', 'Cat')
    Animal3 = Animal('Fido', 'Dog')


    print(Animal1.name)
    print(Animal1.sound)

Main()

