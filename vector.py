
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def length(self):
        return (self.x**2+self.y**2)**(0.5)
    def calibr(self):
        l=self.length()
        self.x=self.x/l
        self.y=self.y/l
    def show(self):
        print('('+str(self.x)+';'+str(self.y)+')')
