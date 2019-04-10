'''
Like dictionaries they contain keys that are hashed to a particular value.
But on contrary, it supports both access from key value and iteration,
the functionality that dictionaries lack.
'''

from collections import namedtuple

## access operation

# declaration
student = namedtuple('Student', ['Name', 'age', 'DOB'])
# add values
s = student('Ayush', '22', '31081996')

# access using index
print(s[0])
# access using keyname
print(s.Name)
# access using getattr()
print(getattr(s, 'DOB'))

'''
._make() :- This function is used to return a namedtuple()
            from the iterable passed as argument.

._asdict() :- This function returns the OrdereDict() as constructed
              from the mapped values of namedtuple().

using “**” (double star) operator :- This function is used to convert a
                                     dictionary into the namedtuple().

'''

li = ['Rajne', '22', '08061996']
e = student._make(li)
print(e)

print(e._asdict())

di = {'Name': 'Niki', 'age': '22', 'DOB': '08061996'}
x = student(**di)
print(x)
