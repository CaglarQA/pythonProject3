
class Person:
    def __init__(self,name:str,age:int):
        self.name=name
        self.age   =age

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Employee(Person):
    def __init__(self,name:str,age:str, job_title:str,company_name:str='Unknown',salary:int=0):
        super().__init__(name, age)
        self.job_title=job_title
        self.company_name=company_name
        self.salary=salary

    def work(self):
        print(f'{self.name} is working')

class Developer(Employee):
    def __init__(self, name: str, age: str, job_title: str ='Soft', company_name: str = 'Unknown', salary: int = 0):
        super().__init__(name, age, job_title)

class Teacher(Employee):

    def __init__(self, name: str, age: str, job_title: str="Teacher", company_name: str = 'Unknown', salary: int = 0):
        super().__init__(name, age, job_title, company_name, salary)

    def work(self):
        print(f'{self.name} is teaching')

employee1=Employee('Hazel',27,'QA','Apple Inc')

developer1=Developer('Daniel',35)

teacher1=Teacher('Ahmet',20,'sef')


print(employee1)
print(developer1)
print(teacher1)

employee1.work()
developer1.work()
teacher1.work()