unique_element=set()


print(type(unique_element))

unique_element.add(10)
unique_element.add(10)
unique_element.add(10)
unique_element.add(20)
unique_element.add(20)
unique_element.add(10)

print(unique_element)  ##{10,20}

#print(unique_element[1])

#print(unique_element[1:])

unique_element.remove(10)

print(unique_element)

unique_element.update((1,2,3,3,1,4,5))

print(unique_element)

unique_element.pop()

print(unique_element)

n = unique_element.pop()

print(unique_element)
print(n)

print('----------------------')

s1={'Java','Python','C#'}
s2={'Rubby','Java','C++','Swift'}


s3=s1.difference(s2)

print(s3)