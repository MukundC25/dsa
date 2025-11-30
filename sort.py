'''numbers = [10, 14, 12, 15, 13, 11]
print("Original:", numbers)
numbers.sort(reverse=True)
print("Sorted (descending):", numbers)'''

##########

#sorts based on length of string
'''def fun(s):
    return len(s)

strings = ["Ram", "Prabhas", "Keerthyy", "Anshka", "Samantha"]
print(strings)
strings.sort(key=fun, reverse=True)
print(strings)'''

############

#sorts in alphabetical order
'''def fun(s):
    return len(s)

strings = ["Ram", "Prabhas", "Keerthyy", "Anshka", "Samantha"]
print(strings)
strings.sort()
print(strings)'''

############

#sorts based on last character of string
'''def fun(s):
    return s[-1]
strings = ["Ram", "Prabhas", "Keerthyy", "Anshka", "Samantha"]
print(strings)
strings.sort(key=fun)
print(strings)'''

############

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

############

'''marks = [60, 30, 50, 20, 10, 40]
print(marks)
sorted(marks)  # returns a new sorted list
print(marks)
print(sorted(marks))  # prints the new sorted list'''

############

'''def fun(n):
    if n>=0: #if positive
        return n
    else:  #if negative
        return -n
numbers = [-10, 14, -12, 15, -13, 11]
new_numbers = sorted(numbers, key=fun)
print(numbers)
print(new_numbers)'''

############

#Stability in sorting algorithms
'''list = [(2, 'aaa'), (1, 'bbb'), (3, 'ccc'), (2, 'ddd'), (1, 'eee'), (3, 'fff')]
print(list)
list.sort()
print(list)'''


#Inplace sorting alogorithm

############

#bubble sort
'''import random
def bubbleSort(list):
    for i in range(len(list)-1): #for i in range of length of list -1
        for j in range(len(list)-i-1): #for comparing adjacent elements
            if list[j]>list[j+1]: #if current element is greater than next element
                #swap
                list[j], list[j+1] = list[j+1], list[j]

list = []
for i in range(10):
    list.append(random.randint(10,99)) #in random module randint fn generate random integer value between the given range
print(list)
bubbleSort(list)
print(list)'''

###########

#iteration for sorted list 
'''import random

c=0
def bubbleSort(list):
    flag = False
    for i in range(len(list)-1): #for i in range of length of list -1
        global c
        c=c+1
        for j in range(len(list)-i-1): #for comparing adjacent elements
            if list[j]>list[j+1]: #if current element is greater than next element
                flag=True #if atleast one swap happens then we set flag to true
                #swap
                list[j], list[j+1] = list[j+1], list[j]
        if flag == False:
                break

list = [10,20,30,40,50,60,70,80,90,100]
print(list)
bubbleSort(list)
print(list)
print("Number of iterations:", c)'''


############

#slection sort
'''import random

def selectionSort(list):
    n = len(list)
    for i in range(n-1):
        min_i = 0
        for j in range(1, n-i):
            if list[j]>list[min_i]:
                min_i = j
        #swap
        list[n-i-1],list[min_i] = list[min_i], list[n-i-1]

list = []
for i in range(10):
    list.append(random.randint(10,99))
print(list)
selectionSort(list)
print(list)'''

############

#insertion sort
'''import random

def insertionSort(list):
    n = len(list)
    for i in range(1, n):
        x = list[i]
        j = i-1
        while j>=0 and x<list[j]:
            list[j+1] = list[j]
            j = j-1
        list[j+1] = x

list = []
for i in range(10):
    list.append(random.randint(10,99))
print(list)
insertionSort(list)
print(list)'''