#Write a Python program to implement a class named Circle with the following requirements:
#The class should contain three instance variables: Radius, Area, and Circumference.
#The class should contain one class variable named PI, initialized to 3.14.
#Define a constructor (init) that initializes all instance variables to 0.0.
#Implement the following instance methods:
#Accept()accepts the radius of the circle from the user.
#CalculateArea() calculates the area of the circle and stores it in the Area variable.
#CalculateCircumference() calculates the circumference of the circle and stores it in the Circumference variable.
#Display() displays the values of Radius, Area, and Circumference.
#Create multiple objects of the Circle class and invoke all the instance methods for each object.

class Circle:
    PI = 3.14

    def __init__(self):
        Radius = 0.0
        Area = 0.0
        Circumference = 0.0
        
    def Accept(self):
        self.Radius = float(input("Enter Radius: "))

    # Calculate area
    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    # Calculate circumference
    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    # Display values
    def Display(self):
        print("\nRadius:", self.Radius)
        print("Area:", self.Area)
        print("Circumference:", self.Circumference)

# Create first object
Obj1 = Circle()
Obj1.Accept()
Obj1.CalculateArea()
Obj1.CalculateCircumference()
Obj1.Display()

# Create second object
Obj2 = Circle()
Obj2.Accept()
Obj2.CalculateArea()
Obj2.CalculateCircumference()
Obj2.Display()