'''1. Write a python script to display the number of days in a given month number.
'''
'''month=int(input("Enter Month Number:"))
match month:
    case 1:
        print("Jan 31")
    case 2:
        print("Feb 28/29")
    case 3:
        print("March 31")
    case 4:
        print("April 30")
    case 5:
        print("May 31")
    case 6:
        print("june 30")
    case 7:
        print("july 31")
    case 8:
        print("August 31")
    case 9:
        print("Sep30")
    case 10:
        print("Oct 31")
    case 11:
        print("Nov 30")
    case 12:
        print("Dec 31")'''
month=int(input("Enter Month Number:"))
match month:
    case month if month in (1,3,5,7,8,10,12):
        print("31 Days")
    case month if month in (4,6,9,11):
         print("30 Days")
    case month if month in (2,):
         print("28/29Days")
    
    case _:
        print("wrong input")
        
