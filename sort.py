'''numbers = [10, 14, 12, 15, 13, 11]
print("Original:", numbers)
numbers.sort(reverse=True)
print("Sorted (descending):", numbers)'''


#sorts based on length of string
'''def fun(s):
    return len(s)

strings = ["Ram", "Prabhas", "Keerthyy", "Anshka", "Samantha"]
print(strings)
strings.sort(key=fun, reverse=True)
print(strings)'''


#sorts in alphabetical order
'''def fun(s):
    return len(s)

strings = ["Ram", "Prabhas", "Keerthyy", "Anshka", "Samantha"]
print(strings)
strings.sort()
print(strings)'''


#sorts based on last character of string
'''def fun(s):
    return s[-1]
strings = ["Ram", "Prabhas", "Keerthyy", "Anshka", "Samantha"]
print(strings)
strings.sort(key=fun)
print(strings)'''


#sorts based on name of student
'''class student:
    def __init__(self, name, htno, marks):
        self.name = name
        self.htno = htno
        self.marks = marks
    
    def __str__(self):
        return f"{self.name}, {self.htno}, {self.marks}"

s1 = student("Ram", "HT001", 85)
s2 = student("Anshka", "HT002", 95)
s3 = student("Keerthyy", "HT003", 90)
s4 = student("Samantha", "HT004", 80)
students = [s1, s2, s3, s4]
print('before sorting:')
for s in students:
    print(s)

# key function to sort student objects by their name
def fun(s):
    return s.name
students.sort(key=fun) #based on name ascending
#students.sort(key=fun, reverse=True) #based on name descending
print('after sorting:')
for s in students:
    print(s)'''


'''marks = [60, 30, 50, 20, 10, 40]
print(marks)
sorted(marks)  # returns a new sorted list
print(marks)
print(sorted(marks))  # prints the new sorted list'''



'''def fun(n):
    if n>=0: #if positive
        return n
    else:  #if negative
        return -n
numbers = [-10, 14, -12, 15, -13, 11]
new_numbers = sorted(numbers, key=fun)
print(numbers)
print(new_numbers)'''

