# Exercise 3(a)
def palindrome(string_val):
    '''Defining a function to check if the returned string is a palindrome or not'''
    try:
        # converting the input string to a lower case
        string_val = string_val.lower()
        # reversing the string and assigning it to a variable
        reverse = "".join(reversed(string_val))
        # checking whether the input and reversed value is the same
        if (string_val == reverse):
            # if both are same then the output is True
            return True
        else:
            # if they dont match then the output is False
            return False
    # Raise exceptions if the user does not input the value
    except:
        print("Error: Enter again")

# print("Ex:3a) Palindrome:")
# # asking input from the user and assigning it to variable
# string_val = input("Enter a string value you would like to check for palindrome condition? ")
# # calling the function
# db = palindrome(string_val)
# # printing whether the result is True or False
# print(f"Is the returned string '{string_val}' a palindrome?  {db}")
# print("\n")

#########################################---------------------------------############################################

# Exercise 3(b)
def max_digit(string_val):
    """Defining a function to get the most occuring frequently occuring letter in a string"""
    try:
        # Iterating values through a string and ignoring non alphabets and numeric, then convert to uppercase
        char_ = "".join([co_unt if co_unt.isalnum() else "" for co_unt in string_val])
        # Converting the characters to uppercase
        char_ = char_.upper()
        # print the alpha numeric string in capitals
        print("Alpha_numeric character in a string is : \n", char_)
        print("*" * 50)
        # max occuring value in the string
        most_frequent_char = max(set(char_), key = char_.count)
        # print the most frequently occuring character in a string
        print("\nThe frequent occuring character in a string is : ", most_frequent_char)
        print("\n*" * 50)
    except:
        print("Error: Input the characters in the space provided")

# print("Ex:3b) Most Frequent letter:")
# # asking the user for the input
# string_val = input("Enter a string: ")
# # calling the function
# max_digit(string_val)
# print("\n")

#########################################---------------------------------############################################

# Exercise 3(c)
def count_param_val(string_val):
    """Writing a function to count the number of letters, spaces and digits entered as a string"""
    try:
        # Initializing zero to a empty dictionary
        param_count = {"_Digits_": 0,
                       "_Spaces_": 0,
                       "_Letters_": 0}
        # Looping through the string
        for count in string_val:
            # Checking if each value of a string is digit or not and adding them to the dictionary
            if count.isdigit():
                param_count["_Digits_"] += 1
            # Checking if each value of a string contains space or not and adding them to the dictionary
            elif count.isspace():
                param_count["_Spaces_"] += 1
            # Checking if each value of a string is alphabet or not and adding them to the dictionary
            elif count.isalpha():
                param_count["_Letters_"] += 1
        # return the values present in the string in a dictionary format
        return param_count
    except:
        print("Error: Enter the string again")

# print("Ex: 3c) Counting letters, Spaces and Digits:")
# string_val = input("Enter a string value of your choice: ")
# db = count_param_val(string_val)
# print("Counts: ",db)

#########################################---------------------------------############################################