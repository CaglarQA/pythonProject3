from  typing import  final

pi :final =3.14

pi=3.5

print(pi)

@final
class Animal:
    pass

class Dog(Animal):
    pass



class Person:

    def __init__(self,age:int):
        self.age=age
