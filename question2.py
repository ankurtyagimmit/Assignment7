'''2. Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division''' 

print("Sum for 1:")
print("Sub for 2:")
print("Mul for 3:")
print("Sum for 4:")
print("Enter your choice:")
choice=int(input())
match choice:
     case 1:
        print("Enter two numbers:")
        a=int(input("Value one:"))
        b=int(input("Volue Two"))
        Result=a+b
        print(Result)
     case 2:
        print("Enter two numbers:")
        a=int(input())
        b=int(input())
        Result=a-b
        print(Result)
     case 3:
        print("Enter two numbers:")
        a=int(input())
        b=int(input())
        Result=a*b
        print(Result)
     case 4:
        print("Enter two numbers:")
        a=int(input())
        b=int(input())
        Result=a/b
        print(Result)
     case 5:
         exit()
     case _:
        print("Sorry you are wrong here!")


