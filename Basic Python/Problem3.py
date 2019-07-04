# Problem Statement: 
# Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. 
# Calculate TOTAL percentage(Not Each subject) and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F
# Assume Each exam has 100 marks in total.




# Taking input of 5 subjects marks- 
p = float(input("Enter marks in Physics: "))
c = float(input("Enter marks in Chemistry: "))
b = float(input("Enter marks in Biology: "))
m = float(input("Enter marks in Math: "))
i = float(input("Enter marks in Computer: "))


TOTAL_marks = p + c + b + m + i
print(f'Total Marks is: {TOTAL_marks}')



# Since each subject has 100 marks. So, 5 subjects will have a total of 500 marks. 
# Calculating total Percentage- 
TOTAL_percentage = (TOTAL_marks*100)/500
print(f'Total Percentage is: {TOTAL_percentage}')


# Calculating Grade- 
if TOTAL_percentage >= 90:
    print("Final Grade is: A")
elif TOTAL_percentage >=80:
    print("Final Grade is: B")
elif TOTAL_percentage >=70:
    print("Final Grade is: C")
elif TOTAL_percentage >=60:
    print("Final Grade is: D")
elif TOTAL_percentage >=40:
    print("Final Grade is: E")
else: 
    print("Final Grade is: F")
