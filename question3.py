'''3. Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.'''
x=input("Enter first value:")
y=input("Enter second value:")
z=input("Enter third value:")
if (x==y or y==z or z==x):
    print("isosceles Triangle")
elif(x==y==z):
    print("equilateral trangle")
else:
    print("right angle triangle")
    exit()
    


