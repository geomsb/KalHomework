class Rectangle:
    def __init__ (self, width = 1, height = 2):
        self.width = width
        self.height = height
#Method
    def getArea(self):
        area = self.width * self.height
        return area
    
    def getPerimeter(self):
        perimeter = (self.width *2) + (self.height*2)
        return perimeter

    def print(self):
        print("width: " + str(self.width) + " height: " + str(self.height) + " area: " + str(self.getArea()) + " perimeter: " + str(self.getPerimeter()))