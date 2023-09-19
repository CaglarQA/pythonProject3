if False :
    print('Python Programing')
    print('Java Programig')

print('C programing')
print('----------------------')

score = 70
if score >=60 :
    pass
print('Congrats! you passed the exam')

"""
if()
"""
s='Hello World'

if 'H' and 'W' in s:
    print(s, 'has', 'H an W')
print('----------------------------')


if score >= 60:
    print('passed')
else:
    print('Failed')

age = 20
result =None

if age >= 21 :
    result= 'Eligible'
else:
    result ='Not eligible'

print('--------------------------')


age = 2
result = 'Eligible' if age >= 21 else 'Not Eligible'

print(result)
print('-------------------------------')
num = 0
result =None
if num > 0:
    result = "Positive"
elif num<0:
    result ="Negative"
else:
    result = "Zero"

print(result)

print('---------------')

num = 200
result2 ='Positive' if num>0   else 'Zero'

print(result2)

print('---------------------------')

score =-500

if 0<= score  <=100:
    if score >=60:
        print('passed')
    else:
        print('Failed')
else:
    print('Invalid Score')

score =75

if 0 <= score<=100:
    if score >=90:
        print('A')
    elif score >=80:
        print('B')
    elif score >=70:
        print('C')
    elif score >=60:
        print('D')
    else:print('F')
else:
    print('Invalid Score')


"""
A score of a student is given, 
"""