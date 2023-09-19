s='Python'

for each in s:
    print(each)
print('-----------------------')

for i in range(0,10):
    print(i)

for i in range(0,len(s)):
    print(s[i])

for i in range (-len(s),0):
    print(s[i])
print('----------------')

#reversed with for
for i in reversed(range(0,len(s))):
    print(s[i])

z='python programing'
result=''
for x in z[::-1]:
    result +=x

print(result)

print('------------------')

num =int( input('Enter a positive number:\n'))
while num <=0:
    num =int (input('Enter a positive number:\n'))

print(f'You have entered {num}')

print('---------------------------------')
