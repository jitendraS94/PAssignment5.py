"""5.	Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?"""
import operator

def basic_4_mathematical_operations():
    print('Select a  number for Arithmetic Operation: \
            \n1 = Addition(+)\
            \n2 = Sub(-)\
            \n3 = Multiplication(*)\
            \n4 = Division(/)\
            \n0 = Stop(0)\n')
    numbers = int(input("Press a number for doing a operation : ="))
    num_1 = int(input('\nEnter 1st Number: '))
    num_2 = int(input('Enter 2nd Number: '))
    if numbers == 0:
        print("Program Stopped successfully")
    elif numbers == 1:
        print(operator.add(num_1,num_2))
    elif numbers == 2:
        print(operator.sub(num_1,num_2))
    elif numbers == 3:
        print(operator.mul(num_1,num_2))
    elif numbers == 4:
        print(operator.truediv(num_1,num_2))
    else:
        print("Please enter a valid number")





basic_4_mathematical_operations()

