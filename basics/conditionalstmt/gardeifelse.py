'''marks = int(input("Enter your marks: "))
if marks < 40:
    print('Grade: F')
elif marks >= 40 and marks < 50:
    print('Grade: P')
elif marks < 60:
    print('Grade: C')
elif marks < 70:
    print('Grade: B')
elif marks < 90:
    print('Grade: A')
else:
    print('Grade: O')'''


age = int(input("Enter your age: "))
if age < 18:
    print(" Not Eligible for Job")
elif age >= 18 and age <= 54:
    print("Eligible for Job")
elif age >= 55 and age <= 59:
    print("Eligible for job but retierment soon")
else:
    print("Retirement Time")