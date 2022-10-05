def findTheHcf(x_term,y_term):
    if x_term>y_term:
        smaller = y_term
    else:
        smaller = x_term
    for ele in range(1,smaller+1):
        if((x_term%ele == 0) and (y_term%ele == 0)):
            hcf = ele
    print(f'The HCF of {x_term},{y_term} is {hcf}')

findTheHcf(6,12)
findTheHcf(2,3)
findTheHcf(10,23)
