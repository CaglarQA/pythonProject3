"""
Java Methods
    public static void method(parameter)

"""

import numbers
def display_message():
    print('Hello Cydeo')
    print('Hello Cydeo')


display_message()


def value():
    return 'Helloo World'


print(value())


def value():
    return 'Python Programing'


print(value())


def return_int() -> int:
    return 10.0


print(return_int())

print('----------------------------------')


def square(num):
    return num * num


print(square(10))


def divide(num1, num2):
    return num1 / num2


print(divide(12, 3))

# print(divide('C#','Python'))

print(square(10))


# print(square('Java'))

def squaree(num: int):
    return num * num


def add(num1: int, num2: int):
    return num1 + num2


print(add(10, 20))

print(squaree(25.5))


def addd(num1: numbers, num2: numbers) -> numbers:
    return num1 + num2


print(add(10, 20))

print(add(10.5 ,20.8))

print('-------------------------------------')

def calculate(num1: numbers, num2: numbers, operator: str)-> numbers:

    if operator == '-':
        return num1-num2
    elif operator =='+':
        return num1+num2
    elif operator == '*':
        return num1*num2
    elif operator == '/':
        return num1/num2
    else:
        print('Invalid operator')
        return 0

print(calculate(10,20,'+'))

print(calculate(100.5, 2.5,'/'))


print('----------method overloading-----------')

#example of method overloading

def sum(n1:numbers,n2:numbers,n3:numbers=0,n4:numbers=0) -> numbers:
    return n1+n2+n3+n4

print(sum(10,20))

print(sum(10,20,30))

print(sum(25,35,45,55))

class test:
    def method(self):
        pass

print('---------------concat----------------')

def concat(a: str,b,c='',d='',e=''):
    print(f'{a}{b}{c}{d}{e}'.strip())

concat('Cydeo', 'School')

concat('Python',3,2.5)
concat('python',3,2.5,True)
concat('Python',3,2.5,True,False)
concat('ada','asa','ala')
e='saas'
print(e)