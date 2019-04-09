import enum

## create an enum

class animal(enum.Enum):
    dog = 1
    cat = 2
    lion = 3

'''
Note:
Member values can be anything: int, str, etc..
If the exact value is unimportant you may use auto instances
and an appropriate value will be chosen for you.
Care must be taken if you mix auto with other values.

class animal is enumeration
animal.dog is enum member
enum members have name and values. 

'''
print('String representation of enum: ', animal.dog)
#The repr() method returns a printable representation of the given object.
print('repr representation: ', repr(animal.dog))
#type
print('type of enum member: ', type(animal.dog))
#name of enum member
print('name: ', animal.dog.name)
#value of enum member
print('value: ', animal.dog.value)


# enumeration object is iterable
for ani in animal:
    print('animal name: ', ani.name)

# enum members can be hashed
ani_sounds = {}
ani_sounds[animal.dog] = 'bark'
ani_sounds[animal.cat] = 'meow'
print(ani_sounds)

# accessing enum members
# by value
print(animal['dog'])
print(animal(3))
