"""4.	Write a Python Program To Find ASCII value of a character?"""

def ASCII_value():
    char = input("Enter the number")
    if len(char) >1:
        print("Please Enter a Single Character")
    else:
        print("ASCII value of a character is ", char,"=",ord(char))

ASCII_value()