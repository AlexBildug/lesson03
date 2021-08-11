# Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
# Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
# Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.

class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def change_name

    def jump(self):
        print(f"{self.name} is jumping")
    def run(self):
        print(f"{self.name} is running")
    def bark(self):
        print(f"{self.name} is barking")

dog = Dog(height=100, weight=50,name="Bobby", age=11)

dog.run()
dog.jump()
dog.bark()

dog2 = Dog(height=150, weight=50,name="Tod", age=7)

dog2.jump()
