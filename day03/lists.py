groceries_list=['Eggs','Milk','Rice']

groceries_list.append('Chicken')

print(len(groceries_list))

groceries_list.extend(('Beef','oranges','Onion'))

print(len(groceries_list))


print(groceries_list)
groceries_list[-2]='Cherry'

print(groceries_list)

print('---------------------------------')

numbers_list=[10,20,30,40,50,60,70,80]

numbers_list[2:-2]=[300,500,5,6000]

print(numbers_list)

print('------------------------------')

characters=['a','b','c','d','e','f','g','h','i']

list1= characters[2:len(characters)-3]

print(list1)

list2=characters[:4]
print(list2)

list3=characters[2:]
print(list3)

characters[2:5]=['C','D','E','C','E','X','Y','Z']

print(characters)

print('-------------------')

names=['Conor','Steve','Hazel','Brenna']

for x in names:
    print(x)

print('------------------------')

nums=[10,20,30,40,50,60]

for i in range(0,len(nums)):
    print(i)

for i in range(0,len(nums)):
    nums[i]/=5
    print(nums)
print('---------------')
print(nums)


nums=[10,20,30,40,50,60]

for i in reversed(range(len(nums))):
    print(nums[i])
print('----------------------------')

for x in nums [::-1]:
    print(x)
print('---------')

for x in reversed(nums):
    print(x)
print('-------------------------')

i=0

while i<len(nums):
    print(nums[i])
    i+=1


print('-------------------------------')

for i in range (1,6):
    i+=2
    print(1)
    print(i)
print('----------------')

nums=[60,500,10,20,15,5,0]

#nums.sort() #ascending order

nums.sort(reverse=True)
print(nums)


print('--------------------')

list1=[10,20,30,40]

list1=list(reversed(list1))

print(list1)

print('-------------------')

tuple_elements = ('Java','Python','C#','Ruby')


list_elements=list(tuple_elements)

print(list_elements)

list1=[1,2,3,4,5]
list2=[1,2,3,4,5]

print(list1 is list2)

tuple1=(1,2,3,4,5)
tuple2=(1,2,3,4,5)

print(tuple1 is tuple2)

groceries_list=['Eggs','Milk','Rice']

print(groceries_list)
groceries_list.append('Chivken')

groceries_list.remove('Milk')
print(groceries_list)

groceries_list.pop()
print(groceries_list)

groceries_list.pop()
print(groceries_list)


groceries_list.insert(2,'Apple')
print(groceries_list)

nums=[1,2,3,4,5,1,1,1,1,5,6,1]

print(nums.count(1))


print('-----------Comprehensions------------------------------')

nums=[]

for x in range(1,51):
    nums.append(x)

print(nums)

print('-------------------------')
"""
divisible_by_5=[]

for x in nums:
    if x % 5 == 0:
        divisible_by_5.append(x)

print(divisible_by_5)

"""

divisible_by_5 =[x for x in nums]
print(divisible_by_5)

divisible_by_5=[x for x in nums if x%5 ==0]

print(divisible_by_5)

divisible_by_5=tuple( [x for x in nums if x%5 ==0])
print(divisible_by_5) #tuple

even_nums=[x for x in nums if x %2==0]
odd_nums=[x for x in nums if x %2 !=0]

print(even_nums)
print(odd_nums)

names =['Python','Java','Java','JavaScript','java','jaVA','Ruby']

names=[x for x in names if x.lower() != 'java']

print(names)


