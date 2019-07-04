# Problem Statement: Write a program to input month number and print number of days in that month.

# Example:
# Input:
# Enter month number: 1

# Output:
# It contains 31 days.

# Month Equivalent Number: January = '1', February = '2', March = '3', April = '4', May = '5', June = '6', July = '7', 
# August = '8', September = '9', October = '10', November = '11', December = '12' 

# January, March, May, July, August, October, December have	31 days
# February has 28/29 days
# April, June, September, November have 30 days


month = int(input("Enter month number: "))

if month >= 1 and month <= 12:
    if month == 1 or month== 3 or month== 5 or month== 7 or month== 8 or month== 10 or month== 12:
        print("It contains 31 days")
    elif month == 2:
        print("It contains 28/29 days")
    else:
        print("It contains 30 days")
        
else:
    print("Invalid Month Number. Please enter number between 1 to 12 to continue!")
