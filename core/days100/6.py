class Mama(object):
    def __init__(self):
        self.s = ''
    def getString(self):
        self.s = input("put something")
    def printString(self):
        print(self.s.upper())

x = Mama()
print(x)

x.getString()
x.printString()