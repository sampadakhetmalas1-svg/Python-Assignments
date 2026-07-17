#Write a Python program to implement a class named Numbers with the following specifications:
#The class should contain one instance variable: Value
#Define a constructor (init) that accepts a number from the user and initializes Value.
#Implement the following instance methods:
#ChkPrime()returns True if the number is prime, otherwise returns False
#ChkPerfect()returns True if the number is perfect, otherwise returns False
#Factors()-displays all factors of the number
#SumFactors() returns the sum of all factors
#Create multiple objects and call all methods.

class Numbers:

    def __init__(self):
        self.Value = int(input("Enter a Number: "))

    # Check Prime Number
    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False

        return True

    # Check Perfect Number
    def ChkPerfect(self):
        sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum += i

        return sum == self.Value

    # Display Factors
    def Factors(self):
        print("Factors are:")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    # Sum of Factors
    def SumFactors(self):
        sum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum += i

        return sum


# First Object
obj1 = Numbers()

print("Prime:", obj1.ChkPrime())
print("Perfect:", obj1.ChkPerfect())
obj1.Factors()
print("Sum of Factors:", obj1.SumFactors())

print()

# Second Object
obj2 = Numbers()

print("Prime:", obj2.ChkPrime())
print("Perfect:", obj2.ChkPerfect())
obj2.Factors()
print("Sum of Factors:", obj2.SumFactors())