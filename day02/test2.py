from utility import sum,calculate
result =sum(10,20)
print(result)


result2=calculate(10,220,'+')
print(result2)


import utility as u

u.concat("java","python")
d=u.sum(44,22)
e=u.calculate(8,9,'*')

print(d,e)

print('---------------------')

from utility import sum as s


print(s(8,9,77))