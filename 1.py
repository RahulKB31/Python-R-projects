# Exercise 1 Program to calculate and output the users age
'''
Example:
Input: Enter your date_of_birth in mm/dd/yyyy: 03/21/1998
Output:
You are 25 years old
Your date_of_birth in European format is : 21/03/1998
'''

from datetime import date

# Taking input from the user
dob = input("Enter your date_of_birth in mm/dd/yyyy: ")

# Creating a class
class age_calc:
    '''Creating a model age calculator'''
    def __init__(self,dob):
        '''Initializing dob attributes'''
        self.dob = dob

    def run_prog(self):
        '''Defining age calculator function'''
        # Try to convert user input into a date object
        try:
            # Converting user input into integer and mapping them to different variables
            month, day, year = map(int, self.dob.split('/'))
            # Assigning the mapped variables into data function and assigning it to a variable
            d = date(year, month, day)
            # Condition to check if the entered date_of_birth is right or not
            if d > date.today():
                print("Error:Entered date_of_birth is in the future.")
            else:
                # Using datetime function to find the present day
                today = date.today()
                # Comparing todays month and day with dob month and day
                t_d = ((today.month, today.day) < (d.month, d.day))
                # Calculating age as per todays date and date_of_birth
                age = today.year - d.year - t_d
                # Output age
                print("You are {} years old".format(age))
                # Output date_of_birth in European format
                print("Your date_of_birth in European format is :", d.strftime('%d/%m/%Y'))
        except ValueError:
            # Invalid user input
            print("Error: Invalid date format")


# if __name__ == "__main__":
#     db = age_calc(dob)
#     db.run_prog()
# Calling the Class age_calc
db = age_calc(dob)
db.run_prog()