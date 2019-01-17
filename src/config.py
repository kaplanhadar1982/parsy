from data_structures import Singleton

class Config(Singleton):

    def __init__(self, c):
        self._c = c


    def printc(self):
        print(self._c)

     