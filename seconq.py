"""2.	Write a Python Program to Find HCF?"""

def Find_HCF():
    num = int(input("Enter the firsht value"))
    num1 = int(input("Enter the firsht value"))
    if num >num1:
        smaller = num1
    else:
        smaller =num
    for i in range(1,smaller+1):
        if ((num%i == 0) and (num1%i == 0)):
            hcf = i
    print("The hcf of",num ,",",num1,"=",hcf)

Find_HCF()
