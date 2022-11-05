class Grandparents:
    height = 180
    age = 60
    sick = "koronovirus"

class Parents(Grandparents):
    age = 40
class Children(Parents):
    height = 170

    def __init__(self):
        print (self.sick)
        print(self.age)
        print(self.height)
daun = Children()
class Wow:
    def _wow(self):
        print ("Wooow")
    def _hello(self):
        print ("Hi!")
some_obj = Wow()
some_obj._hello()
some_obj._wow()

class Hello:
    def __init__(self):
        print("Hi!")
class Hello_World(Hello):
    def __init__(self):
        super().__init__()
        print ("world")
HELLO_WORLD = Hello_World