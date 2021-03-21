class Circle(object):
    pi = 3.14
    def __init__(self):
        # self.r = R1
        # self.r1 = R2

    def area(self,R3):
        self.r = R3
        return self.r
        
        # self.r **2* self.pi*R3
    def area1(self):
        return 100        

cir1 = Circle().area1()
cir2 = Circle(2,4)

print(cir1)

