class s:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class w(s):
    pass
e=w("suman",21)
print(e.age)
