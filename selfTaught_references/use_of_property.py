### Initial class
##class Celsius:
##    def __init__(self, temp = 0):
##        self.temp = temp
##
##    def to_farenh(self):
##        return (self.temp*1.8)+32
##
### Class updated without using property
##class Celsius:
##    def __init__(self, temp = 0):
##        self.set_temp(temp)
##
##    def to_farenh(self):
##        return (self.get_temp()*1.8)+32
##
##    #update
##    def get_temp(self):
##        return self._temp    
##    
##    def set_temp(self, value):
##        if value<-273:
##            raise ValueError('Temp below -273 not accepted')
##        self._temp = value
##
##
### Because of above update the client have to change there code base as well
# Like from obj.temp they have to use obj.set_temp() or obj.get_temp()

# Pythonic implmentation using @property

class Celsius:
    def __init__(self, temp = 0):
        self.temp = temp

    def to_farenh(self):
        return (self.temp*1.8)+32

    #update
    def get_temp(self):
        print('Getting Value')
        return self._temp    
    
    def set_temp(self, value):
        print('Setting Value')
        if value<-273:
            raise ValueError('Temp below -273 not accepted')
        self._temp = value

    temp = property(get_temp, set_temp)

'''
The last line of the code, makes a property object temperature.
Simply put, property attaches some code (get_temperature and set_temperature)
to the member attribute accesses (temperature).

Any code that retrieves the value of temperature will automatically
call get_temperature() instead of a dictionary (__dict__) look-up.
Similarly, any code that assigns a value to temperature will
automatically call set_temperature(). This is one cool feature in Python.

property(fget, fset, fdel, doc)

equivalent code:

temp = property()
temp = temp.getter(get_temp)
temp = temp.setter(set_temp)
'''

## More recommended implementation

class Celsius:
    def __init__(self, temp = 0):
        self.temp = temp

    def to_farenh(self):
        return (self.temp*1.8)+32

    #update
    @property
    def temp(self):
        print('Getting Value')
        return self._temp    

    @temp.setter
    def temp(self, value):
        print('Setting Value')
        if value<-273:
            raise ValueError('Temp below -273 not accepted')
        self._temp = value




        
