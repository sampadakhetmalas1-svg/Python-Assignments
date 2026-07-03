#Accept marks and display grade

marks = int(input("Enter marks :"))



if(marks >= 75 and marks < 100):
    print("Distinction")

elif(marks >= 60 and marks < 75):
    print("Firts Class")

elif(marks >= 50 and marks < 60):
    print("Second Class")

else:
    print("Fail")