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
