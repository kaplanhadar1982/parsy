import abc 

class MyAbc(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def do_something(self,value):
        return NotImplemented

    
    @property
    @abc.abstractmethod
    def some_property(self):
        return NotImplemented




class MyClass(MyAbc):

    def __init__(self, value = None):
        self.__my_prop = value


    def do_something(self,value):
        self.__my_prop *= 2 + value

    @property
    def some_property(self):
        return self.__my_prop


t1 = MyClass(3)
t1.do_something(5)
print(t1.some_property)
