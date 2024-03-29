

class Person:

    def __init__(self,name:'Unknown',age:int=1 ):
        self.__name=None
        self.__age=None
        self.set_name(name)
        self.set_age(age)

    def get_name(self)->str:
        if self.__name==None or self.__name=='' or type(self.__name) !=str:
            raise RuntimeError (f'Invalid name has been set: {self.__name}')

        return self.__name

    def set_name(self,name:str):
        if type(name) !=str:
            raise  RuntimeError(f'Person name must be string')
        if name=='':
            raise RuntimeError(f'Person name can not be emty')

        self.__name=name

    def get_age(self)->int:
        return self.__age

    def set_age(self,age):
        if age <0 or age>150:
            raise  RuntimeError (f'Invalid age  {age}')
        self.__age=age



person1=Person()

print(person1.get_name())
print(person1.get_age())

person2=Person('James')

print(person2.get_name())
print(person2.get_age())

person3=Person('Hazel',27)

print(person3.get_name())
print(person3.get_age())