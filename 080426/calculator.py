print("Welcome to this simple calculator ")
print("Please select from the given options")
print("""
1. for addition
2. for substraction
3. for multiplication
4. for division  
""")
inputSelectedOption=input()
print("Please enter the values\n first value:")
firstvalue=int(input())
print("Please Enter the second value")
secondvalue=int(input())

match inputSelectedOption:
   case "1":
     answer=firstvalue+secondvalue
     print (answer)
   case _:
    print("Over")


  