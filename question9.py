'''9.Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year'''
print("Enter year:")
year=int(input())
match year:
    case year if (year%100!=0):
        print("Not century leap year")
    case year if (year%400==0):
        print("Century leap year")
    case year if (year%4!=0):
        print("Non century non leap year")
    case year if (year%100!=0):
        print("Century non leap year")
'''if(year%400==0 or year%100!=0 and year%4==0):
    print("Leap year")
else:
    print("Not Leap year")'''

