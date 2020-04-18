"""trivial example of duck typing"""
class Animal:
    def __init__(self):
        pass

class Duck(Animal):
    def __init__(self):
        super().__init__()

    def quack(self):
        print("quack")

class Mallard(Duck):
    def __init__(self):
        super().__init__()

class Donald(Duck):
    def __init__(self):
        super().__init__()

class Dog(Animal):
    def __init__(self):
        super().__init__()

def am_i_a_duck(an_animal):
    try:
        an_animal.quack()
        print("I'm a duck!")
    except AttributeError:
        print("no quack method, so can't be a duck, or a duck with a sore throat")

if __name__ == '__main__':
    while True:
        animal = input("enter animal:")
        animal = animal.rstrip().lower()
        if animal == 'duck':
            am_i_a_duck(Duck())
        elif animal == 'mallard':
            am_i_a_duck(Mallard())
        elif animal == 'donald':
            am_i_a_duck(Donald())
        elif animal == 'dog':
            am_i_a_duck(Dog())
        else:
            print("no idea what you are, probably not a duck though!")
            break
