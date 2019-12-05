class Triangle:
    def __init__(self, w, h):
        self.width = w
        self.hight = h
    
    def area(self):
        return self.hight * self.width * 0.5

tri = Triangle(10, 5)
print(tri.area())