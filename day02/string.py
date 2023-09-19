name='Python'
print(len(name))

print(name[0])
print(name[len(name)-1])

print(name[-1])
print(name[-2])

s='Java Programing Language'
s2= s[5:16]
print(s2)

s3=s[:3]
print(s3)

s4=s[:-1]
print(s4)
s5= s[::-1] #reverses the string slicing
print(s5)

s='Python Programing'
r= reversed(s)
print(type(r))

s6=str(r)

print(s6)


s5='Python Programing'
s6=s[7:]
print(s6)

s7='CYDEO SCHOOL'


s8=s7[::-1] #by default
print(s8)

print("-----------------------------------")

#print(help(str))

s='python programing language'

s=s.capitalize()
print(s)

s=s.title()
print(s)

s="     Python             "
print(s)
s=s.strip()
print(s)

s='JAVA ABA'

print(s.index('A'))

print(s.rindex('A'))

s='Java Java'

s=s.replace('Java','Python')
print(s)


s='Java Java'

s=s.replace('Java','Python',1)
print(s)

s='C# C# Python'
s=s.replace(' C# ', 'Java ')
print(s)

s='Java Java Java Python Python python Java java python'

count_java =s.count('Java')
print(count_java)

count_python=s.count('Python')
print(count_python)

s1='java'
s2='JAVA'

print(s1==s2)#false

print(s1.lower()==s2.lower()) #ignore case

s= 'Java'
print(s.islower())
print(s[0].islower())
print(s[1].islower())
print(s[0].isupper())

print(s.isalpha())

s='Cydeo School '
