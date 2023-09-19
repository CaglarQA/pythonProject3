days=("Mon",'Tue',"Wednesday",'Thusday',"Frday","Saturday",'Sunday',1,2,3,4,5,6,7,True,False)

print(type(days))
print(len(days))

print(days)

#days[0]='Java'
#print(days)

print(days[0])
print(days[-1])

day=("mon","tue","wed","thu","fri","sat","sun")
work_days=day[1:-5]
print(work_days)
work_days2=day[1:4]
print(work_days2)

weekend=day[-3:]
print(weekend)

tuple1=(1,2,3)
tuple2=(1,2,3)

print(tuple1==tuple2)
print(tuple1 is tuple2)

tuple3=tuple1+tuple2

print(tuple3)
tuple4=tuple1*5
print(tuple4)



reversed_tuple=day[::-1]
print(reversed_tuple)

reversed_tuple2= tuple(reversed(day))
print(reversed_tuple2)

print(day.index('wed'))


numbers=(10,10,10,10,20,30,40,50,10)

print(numbers.count(10))


print('----------------------------------------')
for x in day:
    print( x)

print('---------------')
for x in range (0, len(day)):
    print(x)

print('----------------')

for  x in reversed(range(0,len(day))):
    print(x)

print('-------------')

nested_tuple=((1,2,3),(4,5,6,7,8),(9,10))

print(len(nested_tuple))

print('----------')
for x in nested_tuple:
    print(x)

print('------')
for x in nested_tuple:
    print(x)
    for y in x:
        print(y)

print('--------------------------')

#for i in range(0, len(nested_tuple[i])):
