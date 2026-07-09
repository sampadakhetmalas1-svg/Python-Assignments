def CheckPrime(no):
    
    if no<=1:
        return "Number Should be Positive"
    
    for i in range(2,no):

        if no % i == 0:
            return False
        
    return True

