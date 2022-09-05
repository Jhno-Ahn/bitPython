# mymodule.py
__version__ = 1.0
def hello() :
    print( "안녕하세요" )
def bye() :
    print( "안녕히계세요" )
class User :
    def __init__(self, name="", age=0 ) :
        self.name = name
        self.age = age
    def getName(self) :
        return self.name
    def getAge(self) :
        return self.age         