#Ask the user to input their full name & perform a valdation to check that the user has entered a full name
#If the user has not entered a full name, ask them to enter their full name again
#If the user has entered less than 4 characters, ask them to enter their full name again
#If the user has entered more than 25 characters, ask them to enter their full name again
#If the user has entered a full name, print out the first name and last name and thank them for using the program

name = input("Please enter your full name: ")
if len(name) < 4:
    print("Your name is too short. Please enter your full name.")
elif len(name) > 25:
    print("Your name is too long. Please enter your full name.")
else:
    print("Thank you for using the program. Your full name is: " + name)