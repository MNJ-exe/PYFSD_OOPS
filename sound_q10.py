class Sound():
    def __init__(self):
        pass
class Dog(Sound):
    def make_sound(self):
        print("Dog barks!")
class Cat(Sound):
    def make_sound(self):
        print("Cat meows!")
for s in [Dog(),Cat()]:
    s.make_sound()