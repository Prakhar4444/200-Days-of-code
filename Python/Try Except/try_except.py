try:
#   value = 10/0
    number = int(input("Enter a number"))
    print ((number))
except ZeroDivisionError as e1:
    print ("Divided by Zero " + str(e1))
except ValueError as e2:
    print ("Invalid Input " + str(e2))