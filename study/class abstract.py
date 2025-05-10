class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def move(self):
        print("Moving around")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")