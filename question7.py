'''7. Write a python program to check whether a given number is positive, negative or
zero using match case statement'''
number=int(input("Enter a number:"))
match number:
    case number if number>0:
        print("Positive")
    case number if number<0:
        print("negative")
    case number if number==0:
        print("Zero")
