'''6. Write a python program to check whether a given string is a multiword string or single
word string using match case statement'''
S=str(input("Enter any string word:"))
S.strip()
match S:
    
    case S if ' ' in S:
         print("multiword string")
            
    case S if ' ' not in S:
         print("single wordn string")
           
        
    
