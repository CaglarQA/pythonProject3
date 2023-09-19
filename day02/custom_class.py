import numbers
class Employee:
    is_human=True #similar to static variable of java
    planet='Earth'
    def __init__(self,name:str ='Unknown',job_title:str ='Janitoe',salary:numbers =0):
        self.name = name
        self.job_title=job_title
        self.salary=salary

    def work(self):
        print(f'{self.name} is working')

    def __str__(self):
        return f'name:{self.name}, job_title:{self.job_title}'

employee1=Employee()

print(employee1.name)
print(employee1.job_title)
print(employee1.salary)

print('-------Emplolyee 2-------------')

employee2=Employee('Daniel')
print(employee2.name)
print(employee2.job_title)
print(employee2.salary)

print('---Emplypee 3--------')
employee3= Employee('Brenna','Sdet')

print(employee3.name)
print(employee3.job_title)

print('------------employee 4 --------------------')
employee4=Employee('Yulia','Python',150_000)

print(employee4.name)
print(employee4.job_title)
print(employee4.salary)

print('----------------------')
print(employee4.is_human)
print(employee2.planet)

employee1.work()
employee2.work()
employee3.work()
employee4.work()


print(employee1)
print(employee2)
print(employee3)
print(employee4)