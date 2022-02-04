'''
Task 1
User wants to visit our shop and wants to know about possibility to do that and existing discount. Write a code that will ask current time (hours only), age and the gender of a user and will write "**Closed**" if user cannot visit our shop and "**Opened. Discount is *DISCOUNT*%**"
Shop is opened from 9AM till 11PM.
Availability and discounts of shop:

|Time|Age|Gender|Discount|IsOpened
|-|-|-|-|-
|9-16|18|M|10%|True
|9-16|18|F|0%|False
|16-23|18|M|0%|False
|16-23|18|F|10%|True
|10-15|<18|M|20%|True
|10-15|<18|F|20%|True
|18-20|<18|M|5%|True
|18-20|<18|F|5%|True

Time ranges are not inclusive (if time range is 9-11 - the rules are applied to the following hour values: [9, 10])
'''

time = int(input("Time"))
age = int(input("Age"))
gender = input("Gender (M/F)")
gender.lower()
if time in range (9,16) and age == 18 and gender == 'm':
    print("Opened. Discount is 10%")
elif time in range (16,23) and age == 18 and gender == 'f':
    print("Opened. Discount is 10%")
elif time in range (10,15) and age < 18:
    print("Opened. Discount is 20%")
elif time in range (18,20) and age < 18:
    print("Opened. Discount is 5%")
else:
    print("Closed")

'''
Task 2
Binary search
Ask user for number from 1 to 10 (inclusive), if user inputs wrong number - write "error". 
If user typed in a valid number - write a number from the middle of a known range and ask for comparsion ("<", ">", "=") 
and perform further search if required. 
TIP Do not use loops if you are familiar with them.
'''

number = int(input("Please write a number from 1 to 10"))
if number in range (1,11):
    sign = (input("Is your number 5? Write = if so, > if it is greater or < if smaller")
    if sign == "=":
        print("Your number is 5")
    elif sign == "<":
        sign = (input("Is your number 2? Write = if so, > if it is greater or < if smaller")
        if sign == "=":
            print("Your number is 2")
        elif sign == "<":
            print("Your number is 1")
        elif sign == ">":
            sign = (input("Is your number 3? Write = if so, > if it is greater or < if smaller")
            if sign == "=":
                print("Your number is 3")
            elif == ">":
                print("Your number is 4")
            else:
                print("Error")
        else:
            print("Error")
    elif sign == ">":
        sign = (input("Is your number 8? Write = if so, > if it is greater or < if smaller")
        if sign == "=":
            print("Your number is 8")
        elif sign == "<":
            sign = (input("Is your number 6? Write = if so, > if it is greater or < if smaller")
            if sign == "=":
                print("Your number is 6")
            elif sign == ">":
                print("Your number is 7")
            else:
                print("Error")
        elif sign == ">":
            sign = (input("Is your number 9? Write = if so, > if it is greater or < if smaller")
            if sign == "=":
                print("Your number is 9")
            elif sign == ">":
                    print("Your number is 10")
            else:
                    print("Error")
        else:
            print("Error")
    else:
        print("Error")   
else:
    print("Error")

'''
Task 3
Bitwise operators
Implement flags for keeping weather state. We want to know, was it snowy / rainy / cloudy / hail / fog
'''

flags_var = 0
snowy = 0b1
rainy = 0b10
cloudy = 0b100
hail = 0b1000
fog = 0b10000
if input("Is it snowy? Please write y or n") == 'y':
    flags_var +=snowy
if input("Is it rainy? Please write y or n") == 'y':
    flags_var +=rainy
if input("Is it cloudy? Please write y or n") == 'y':
    flags_var +=cloudy
if input("Is it hail? Please write y or n") == 'y':
    flags_var +=hail
if input("Is it fog? Please write y or n") == 'y':
    flags_var +=fog
print("Weather now: ")
if snowy & flags_var:
    print("snowy")
if rainy & flags_var:
    print("rainy")
if cloudy & flags_var:
    print("cloudy")
if hail & flags_var:
    print("hail")
if fog & flags_var:
    print("fog")
