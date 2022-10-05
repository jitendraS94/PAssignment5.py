"""1.	Write a Python Program to Find LCM?"""

def Find_LCM():
    num = int(input("Enter the firsht value"))
    num1 = int(input("Enter the firsht value"))
    if num > num1:
        greater = num
    else:
        greater  = num1
    while True:
        if((greater%num == 0) and (greater%num1 ==0)):
            lcm = greater
            break
        else:
            greater += 1
    print("The lcm of",num ,",",num1,"=",lcm)

Find_LCM()
