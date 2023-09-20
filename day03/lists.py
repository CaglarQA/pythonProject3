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

