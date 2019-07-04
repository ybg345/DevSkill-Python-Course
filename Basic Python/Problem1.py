# Problem Statement: Write a program to find maximum,minimum,mean between three numbers.



a = int(input("Enter first number: "))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

# Maximum among 3 numbers: 
if a>b:
    if a>c:
        print(f'{a} is the maximum number')
    else:
        print(f'{c} is the maximum number')
else:
    if b>c:
        print(f'{b} is the maximum number')
    else:
        print(f'{c} is the maximum number')


# Minimum among 3 numbers: 
if a<b:
    if a<c:
        print(f'{a} is the minimum number')
    else:
        print(f'{c} is the minimum number')
else:
    if b<c:
        print(f'{b} is the mimimum number')
    else:
        print(f'{c} is the minimum number')


# Mean of three numbers: 
mean = (a+b+c)/3
print(f'Mean of the three number is {mean}')