# create a module named as Arithmetic which contains 4 fun as Add(),Sub()
# Mult() and Div() all funs accepts two parameters as number 
# and perform the operation.write on python program which call all the funs
#  from stithmeetic module by accepting the parameters from user
import Arithmetic

def main():

    No1 = int(input("Enter first number:"))
    No2 = int(input("Enter Second number :"))
        

    print("Addition is : ",Arithmetic.Add(No1,No2))
    print("Substraction is : ",Arithmetic.Sub(No1,No2))
    print("Multiplication is : ",Arithmetic.Mul(No1,No2))
    print("Division is : ",Arithmetic.Div(No1,No2))

if __name__ == "__main__":
    main()