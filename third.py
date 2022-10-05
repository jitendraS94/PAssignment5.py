"""3.	Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?"""

def DecimalToOther():
    num = int(input('Enter a Number: '))
    print("Binary num is :=",bin(num))
    print("Octal num is",oct(num))
    print("Hexadecimal num is",hex(num))

DecimalToOther()