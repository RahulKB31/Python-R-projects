# Exercise 5
'''
Example:
Input:
> Enter the File Name you want to open?:  student_data.txt
....The fileName student_data.txt exist :)....
> Please Enter the output File_Name: output_File.txt
....The file name rk has been created :D....
Output:
- Number of Students who received First class marks: 36
- Number of Students who received Second class marks: 23
- Number of Students who received Third class marks: 21
- Number of Students who have Failed: 20
**************************************************
> Registration number of students failed:-
[2099309, 2092266, 2067524, 2176075, 2125759, 1932827, 2003492, 1971335,
1963755, 1882149, 1975305, 1871813, 2168985, 1992226, 2116305, 2083148,
1962016, 2022465, 2105013, 2170785]
'''

#pip install numpy
import numpy as np
# User should Input the file name that need to be opened
# Here the file is named as (student_data.txt)
f_name = input("> Enter the File Name you want to open?:  ")

#creating a class name called University student
class Uni_stu_Dent:
    '''Intializing the class to registration number, exam mark, course work mark, coursework weightage'''
    def __init__(self, r_n, e_mk, cw_mk, cw_wt):
        self.r_n = r_n        # registration number
        self.e_mk = e_mk      # exam_mark
        self.cw_mk = cw_mk    # coursework_mark
        self.cw_wt = cw_wt    # coursework weightage
        self.ov_MK = round((1 - cw_wt) * e_mk + cw_wt * cw_mk)    # overmark
        self.grade = self.calc_Grade()    # grade

    def read_file(f_name):
        '''Defining a function to read the input file and perform specific operations'''
        try:
            with open(f_name, "r") as fn:
                # Tells the user that input file exist and continues with the operation
                print(f"....The fileName {f_name} exist :)....\n")
                # Reads the first line
                a = fn.readline()
                # Splits the strings into multiple strings
                b = a.split()
                # Assigning variable to the 1st line
                no_of_students = int(b[0])            #100
                # Weightage of marks
                cw_wt = int(b[1]) / 100               #30
                # Creating an empty array list with respect to the number of students present
                r_1 = np.array([[0, 0.0, 0.0, 0.0]] * no_of_students)
                # Performing iterations on the number of students present
                for l in range(no_of_students):
                    # Reads the 1st line
                    a = fn.readline()
                    # Strips the string based on blank space
                    b = a.strip()
                    # Splits the string into multiple substrings
                    c = b.split()
                    # Converting and storing all the values in the 1st column to an integer
                    r_n = int(c[0])
                    # Converting and storing all the values in the second column as floating point numbers
                    e_mk = float(c[1])
                    # Converting and storing all the values in the 3rd column as floating point numbers
                    cw_mk = float(c[2])
                    # Assigning these values to empty string created, row by row
                    r_1[l] = [r_n, e_mk, cw_mk, 0.0]
            # Defining a named data type which contains four integers and one string
            stuD_Type = np.dtype([('r_n', int), ('e_mark', int), ('cw_mk', int), ('ov_MK', int), ('grade', 'U2')])
            # greade string to be calculated and store them in the corresponding array
            stuD = np.array([(0, 0, 0, 0, '')] * no_of_students, dtype=stuD_Type)
            # Intializing i to zero
            i = 0
            # Looping till i is equal to number of students
            while i < no_of_students:
                # assigning the values to the arrays using class function
                s = Uni_stu_Dent(r_1[i][0], r_1[i][1], r_1[i][2], cw_wt)
                # Calculating the overall marks using the coursework weightage, performing operation from the intializer function
                overall_Mark = s.ov_MK
                # Intializing grade based on the over all marks calculated, grading function is defined above
                g = s.grade
                # Assigning values to the numpy datatype
                stuD[i] = ((r_1[i][0], r_1[i][1], r_1[i][2], overall_Mark, g))
                # After looping through the entire row, set i to next number and repeat the loop, repeats the operation till i = 100
                i+=1

            # After grading sorting is done based on the highest marks obtained in the descending order
            m_SoRT_LisT = np.sort(stuD, order='ov_MK')[::-1]
            # Enter the name of your out[ut file
            output = input("\n> Please Enter the output File_Name: ")
            # Open a new file and store new set of data of students based on their overall marks
            with open(output, 'w') as f2:
                # Inform the user that output file has been created
                print(f"....The file name {output} has been created :D....\n")
                # print them inside the file
                print(m_SoRT_LisT, file=f2)
                # Create an empty list n1
                n1 = []
                # Iterate through each row
                for s in m_SoRT_LisT:
                    # Check whether the student has got above 70 marks
                    if s[4] == 'A':
                        # If yes, append to the list
                        n1.append(s)
                # print the number of students who receive above 70 marks
                print("- Number of Students who received First class marks: {}".format(len(n1)))
                # Create an empty list n2
                n2 = []
                # Iterate through each row
                for s in m_SoRT_LisT:
                    # Check whether the student has got above 60 and bel0w 70 marks
                    if s[4] == 'B':
                        # If yes, append to the list
                        n2.append(s)
                # print the number of students who receive above 60 and bel0w 70 marks
                print("- Number of Students who received Second class marks: {}".format(len(n2)))
                # Create an empty list n3
                n3 = []
                # Iterate through each row
                for s in m_SoRT_LisT:
                    # Check whether the student has got above 50 and bel0w 60 marks
                    if s[4] == 'C':
                        # If yes, append to the list
                        n3.append(s)
                # print the number of students who receive above 50 and bel0w 60 marks
                print("- Number of Students who received Third class marks: {}".format(len(n3)))
                # Create an empty list n4
                n4 = []
                # Iterate through each row
                for s in m_SoRT_LisT:
                    # Check how many students has got below 50 marks
                    if s[4] == 'F':
                        # If yes, append to the list
                        n4.append(s)
                # print the number of students who failed
                print("- Number of Students who have Failed: {}\n".format(len(n4)))
                # print
                print("*" * 50)
                print("\n> Registration number of students failed:- \n")
                # Create an empty list n5
                n5 = []
                # Iterate through each row
                for s in m_SoRT_LisT:
                    # Check which student has got below 50 marks
                    if s[4] == 'F':
                        # If yes, append to the list
                        n5.append(s[0])
                # print the registration number of students who have failed
                print(n5)
        # If the input file does not exist raise exceptions
        except FileNotFoundError:
            print(f"The Input file {f_name} name does not Exist. Please try again :(")

    # Defining a function for grading according to overall marks
    def calc_Grade(self):
        try:
            if self.ov_MK >= 70:  # If marks is above 70
                return "A"
            elif self.ov_MK >= 60:  # If marks is greater than 60
                return "B"
            elif self.ov_MK >= 50:  # If marks is greater than 50
                return "C"
            elif self.ov_MK > 100:
                raise Exception
            else:
                return "F"  # Return fail if marks is below 50
        except IOError:
            print("Please repeat the operations line by line")

# Calling the Module
# if __name__ == '__main__':
Uni_stu_Dent.read_file(f_name)