'''
Program: WAP to calculate and display factorial of a given number
Author: Bikramadittya Bagchi
Date: 08-02-2021
'''

num = int(input("Enter no. to print factorial: "))
f = 1
if num < 0:
    print("Factorial is only defined for non-negative numbers")
elif num == 0:
    print(f"Factorial of {num} = {f}")
else:
    for i in range(1, num+1):
        f = f * i
    print(f"Factorial of {num} = {f}")