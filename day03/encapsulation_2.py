
class Person:

    def __init__(self):
        self.__name =None
        self.__age =None


    @property
    def  person_name(self):
        return self.__name

    @person_name.setter
    def person_name(self,value):
