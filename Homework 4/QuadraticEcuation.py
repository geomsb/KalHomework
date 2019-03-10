class QuadraticEquation:
    def __init__(self, a, b, c):
        self.__a = a 
        self.__b = b
        self.__c = c 

#Accesor methods
    def getA (self, a):
        return self.__a 
    
    def getB (self, b):
        return self.__b

    def getC (self,c):
        return self.__c

#Methods

    def getDiscriminant(self):
        discriminant = (self.__b**2)-(4*self.__a*self.__c)
        return discriminant

    def getRoot1(self):
        if self.getDiscriminant() < 0:
            return 0
        else:
            root1 = (-self.__b -(self.getDiscriminant()**.5)) / (2*self.__a)
            return root1

    def getRoot2(self):
        if self.getDiscriminant() < 0:
            return 0
        else:
            root2 = (-self.__b +(self.getDiscriminant()**.5)) / (2*self.__a)
            return root2
    
    def display(self): 
        if self.getDiscriminant () > 0:
            print (self.getRoot1())
            print (self.getRoot2())
        if self.getDiscriminant() == 0:
            print (self.getRoot1)
        if self.getDiscriminant() < 0:
            print("The equation has no roots")
