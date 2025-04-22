class Animalheri: #parent class
    alive=True
    def eat(self):
        print("This Animal is eating")
    def slumber(self):
        print("This Animal is sleeping")

class Rabbit(Animalheri):#Child1 class
    def run(self):
        print("The Rabbit is running very fast.")
class Fish(Animalheri):#Child2 class
     def swim(self):
        print("This Fish is swimming in the water.")
class Hawk(Animalheri):  # Child3 class
    def fly(self):
        print("This Hawk is flying very high.")

rabbit=Rabbit()
fish=Fish()
hawk=Hawk()

#print(rabbit.alive)
#fish.eat()
#hawk.slumber()

rabbit.run()
fish.swim()
hawk.fly()
