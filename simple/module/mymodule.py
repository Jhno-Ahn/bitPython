# mymodule.py
__version__ = 1.0
def hello():
    print("안녕하세여ㅑ")
def bye():
    print("바이여")
class User:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age