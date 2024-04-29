#Data Types

#String
print("Hello"[0])
print("123"+"345")

#Integer
print(123 + 345)

#to make the number more readible to human like 10,000
#the computer will ignore the 10_000

#Float
3.14159

#Boolean
True
False

num_char = len(input("What is your name"))
# print("Your name has "+ num_char + "characters.")

print(type(num_char))

new_num_char = str(num_char)
print("Your name has "+ new_num_char + "characters.")

a = str(123)
print(type(a))

#this convert the "str" to float integer then plus it]
print(70 + float("100.5"))

#just the str 70100
print(str(70) + str(100))

#Exercise 1
""" Write a program that adds the digits 
in a 2 digit number. e.g. if the input was 35, 
then the output should be 3 + 5 = 8"""
two_digit_number = input()
# split the number into 2 digit and plus them
a = int(two_digit_number[0])
b = int(two_digit_number[1])

sum = a + b

print(sum)

#Mathematical Operations in Python
"""
3 + 5
10 - 5
3 * 2
6 / 3
** #exponents 
2 ** 3 #2 to the power of 3
"""


"""
PEMDAS order
()
**
* /
+ -
"""


#Exercise 2 - BMI Calculator

# 1st input: enter height in meters e.g: 1.65
height = float(input())
# 2nd input: enter weight in kilograms e.g: 72
weight = int(input())
BMI = weight/(height**2)
print(int(BMI))

# round the decimal point
print(round(8/3))

#round by 2 decimal point
print(round(8/3, 2)) 

#turn float into int straigthaway 
print(8//3)

result = 4/2
result /= 2

#user scores a point
score += 1
print(score)

your_score = 0
your_height = 1.8
isWinning = True
#f-string
# print("your score is" + str(your_score))
print(f"your score is {your_score}, your height is {your_height}, you are winning is {isWinning}")

#Exercise 3 - time left in weeks 
"""I was reading this article by Tim Urban - 
Your Life in Weeks and realised just how little time we actually have.

Create a program using maths and f-Strings that 
tells us how many weeks we have left, if we live until 90 years old."""
age = input()
#assuming that we live up to 90 y/0
time_left = 90 - int(age)
#about 52 weeks
weeks_per_year = int(365/7)
age_to_weeks = int(time_left)* weeks_per_year
print(f"You have {age_to_weeks} weeks left.")

#Final Challenge - a Tip calculator
print("Welcome to the tip calculator\n")
Total_Bill = float(input("What was the total bill? $"))
Tip_percent = int(input("How much tip would like to give? 10, 12, or 15 "))
Number_of_people = int(input("How many people to split the bill? "))
Calculate_percent = Tip_percent/100
Add_tip_bill = (Total_Bill*Calculate_percent) + Total_Bill
Split_people = round(Add_tip_bill/Number_of_people, 2)
Split_people = "{:.2f}".format(Add_tip_bill/Number_of_people)
print(f" Each person should pay: ${Split_people}")
