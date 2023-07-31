# Exercise 4

'''
Input:
> Enter a filename: data.txt
> Enter the bottom salary range: 200
> Enter the top salary range: 200000
'''

class emp_db:
    '''Creating a parent class and defining different functions inside them'''

    # Initializing the function
    def __init__(self, file_name):
        self.emply = []
        self.open_file(file_name)

    def salary_func(self, sal1, sal2):
        """Defining a salary function which outputs name, job title and salary based on the input salary range"""
        try:
            # Creating an empty list
            filtered_list = []
            # Iterating through the list from the file
            for i in self.emply:
                # Assigning names to each variables in the list
                name, job_title, salary = i
                # checking if it is present in the salary range and appending it to the list
                if sal1 <= salary <= sal2:
                    filtered_list.append((salary, name.upper(), job_title.upper()))
                else:
                    # rasie exceptions
                    raise IOError
            # sorting the list in the descending order
            filtered_list.sort(reverse=True)
            # checking the length of the list
            if len(filtered_list) == 0:
                raise IOError
            else:
                # printing the column names
                print(f"{'Salary':<20} | {'Name':<10} | {'Job Title':<10}")
                print("-" * 50)
                # Iterating through each list and printing the desired values under respective column names
                for i in filtered_list:
                    salary, name, job_title = i
                    print(f"{salary:<20} | {name:<10} | {job_title:<10}")
                    print("-" * 50)
                print("\n")
        # Raising exceptions if the salary if out of range
        except IOError:
            print(f"No employees are found in the salary ranges between {sal1} and {sal2}")

    def open_file(self, file_name):
        '''Defining a function to read the file'''
        while True:
            try:
                with open(file_name, 'r') as file:
                    # looping through each line of a file
                    for i in file.readlines():
                        # stripping through each lines of a file and splitting them at comma seperated values and assigning them to variable name
                        name, job_title, salary = i.strip().split(",")
                        # converting string to a integer for comparing the ranges
                        salary = int(salary)
                        # assigning them to a  variable
                        emp = (name, job_title, salary)
                        # appending the variables to a empty list
                        self.emply.append(emp)
                    break
            # rasing exceptions when the input filename is not present
            except FileNotFoundError:
                print(f"File not found: {file_name}")
                file_name = input("> Enter a filename: ")
            # closing the file after all functions are performed
            finally:
                file.close()

    def output(self):
        '''Defining a function for user input and calling the other functions from the userr input'''
        while True:
            # Taking user input for the bottom and top salary ranges
            sal1 = int(input("> Enter the bottom salary range: "))
            sal2 = int(input("> Enter the top salary range: "))
            print("*" * 50)
            print("\n")
            # passing the user input to the salary_function
            emply_db.salary_func(sal1, sal2)
            # Asking input from the user if they want to continue or quit
            c = input("> Do you want to continue or quit (Y/N)? ")
            if c.lower() == 'n':
                print(">>> >>> quit")
                break


# Asking user to input filename
file_name = input("> Enter a filename: ")
# assigning the class to a variable
emply_db = emp_db(file_name)
# calling the functions
emply_db.open_file(file_name)
emply_db.output()