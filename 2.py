# Exercise 2. Write a function that returns list of all non prime numbers
'''
Example: Input : number1 = 20, number2 = 100
Output:
20  21  22  24  25  26  27  28  30  32
33  34  35  36  38  39  40  42  44  45
46  48  49  50  51  52  54  55  56  57
58  60  62  63  64  65  66  68  69  70
72  74  75  76  77  78  80  81  82  84
85  86  87  88  90  91  92  93  94  95
96  98  99  100  '''

"""Taking inputs from the user and assign it to the variables"""
number1 = int(input("Enter the first positive integer: "))
number2 = int(input("Enter the second positive integer: "))

# Choosing the starting and ending points in a function by min and max function
starting = min(number1, number2)
ending = max(number1, number2)

'''Creating a  model which returns non prime numbers'''

class numbers:
    '''Initializing starting and ending points'''

    def __init__(self, starting, ending):
        self.starting = starting
        self.ending = ending

    '''Defining a function which returns non prime numbers'''

    def non_prime_numbers(self):
        try:
            # creating a empty list
            list_np = []
            # looping through the ranges
            for val in range(starting, ending + 1):
                # Raising exception if the value is less than 1
                if val <= 1:
                    raise ValueError
                else:
                    # condition to check if the values in the range is non prime and appending it
                    for x in range(2, val):
                        # checking whether the value is non prime
                        if val % x == 0:
                            # appending the values to a empty list
                            list_np.append(val)
                            break
            # return the list of non prime after appending
            return list_np
        # raise exception if there is error with the user input
        except ValueError:
            print("Error: Enter positive integer greater than 1")

    '''Defining the function for outputing 10 non prime numbers in a line'''

    def output(self):
        # checking if the user input is less than 0
        try:
            if starting <= 0 or ending <= 0:
                # rasing exception if the user input is less than or equal to 0
                raise ValueError
            else:
                # assigning class function to a variable
                enum = numbers(starting, ending)
                # calling the function from inside the class
                list_np = enum.non_prime_numbers()
                # enumerating the list from the list of non primes
                for x, y in enumerate(list_np, 1):
                    print(y, end="  ")
                    # condition to enter only 10 values in a line
                    if x % 10 == 0:
                        # print the non prime numbers
                        print()
        # raising an exception is the value is less than 1 and negative
        except ValueError:
            print("Error: Entered Value must be greater than 1 and positive")


# calling the model class
# if __name__ == "__main__":
#     db = numbers(starting, ending)
#     db.output()

# calling the model class
db = numbers(starting, ending)
db.output()