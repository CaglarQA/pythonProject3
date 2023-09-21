
try:
    num =10/0

    print(num)

except:
    print('Soemthing went wrong')
else:
    print('Nothing went wrong')
finally:
    print('finaly block')
print('Test Completed')



print('-------------------------------')

tuple1=(10,20,30,40)

try:
    print(tuple1[200])

except LookupError:
    print('The index number is too large')
else:
    print('The index number is valid')

print('-----------------------------------')

try:
    raise FileNotFoundError('No such a file')
except SyntaxError:
    print("It is a syntax error")
except OSError:
    print('It is an operating system error')

except ArithmeticError:
    print('It is an arithmetic error')
finally:
    print('Finally block')

print('----------------------------------------')

raise  LookupError('Invalid entry')

"""
Java
    throw used for manually throwing exception
    throws: for exception handings (in method signature)
"""


