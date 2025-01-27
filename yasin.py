# # Exercise 34
# # Creating user input for integer
# pro = int(input("Enter a number: "))
# # If statement to determine if number is odd or even
# if pro % 2 == 0:
#     print(pro, "is even")
# else:
#     print(pro, "is odd")

# # Exercise 35
# # Creating user input for human years
# humanYears = float(input("Enter the number of human years :"))
# # if statement to determine dog years
# if humanYears <= 2:
#     dogYears = humanYears * 10.5
# # else statement adds 21 which is first two dog years which subtracts 2 from human years the multiplies 7
# else:
#     dogYears = 21 + (humanYears - 2) * 7
# # printing dog years
# print("The equivalent number of dog years is", dogYears)

# # Exercise 36
# # User input for vowel which is v
# v = input("Enter a letter :").lower()
# # If statement to make sure the letter is equal to a vowel
# if v == "a" or v == "e" or v == "i" or v == "o" or v == "u":
#     print("This is a vowel")
# elif v == "y":
#     print("y is sometimes a vowel and sometimes a constant")
# else :
#     print("This is not a vowel")

# # Exercise 37
# # Creating user input for number of sides
# sides = int(input("Enter a number of sides for a shape (3-10) :"))
# # if statement that checks number and displays appropriate shape
# if sides == 3 :
#     print("This is a triangle")
# elif sides == 4 :
#     print("This is a quadrilateral")
# elif sides == 5 :
#     print("This is a pentagon")
# elif sides == 6 :
#     print("This is a hexagon")
# elif sides == 7 :
#     print("This is a heptagon")
# elif sides == 8 :
#     print("This is a octogon")
# elif sides == 9 :
#     print("This is a nonogon")
# elif sides == 10 :
#     print("This is a decagon")
# else :
#     print("Please enter a number of sides 3-10")

# # Exercise 38
# #User input for month. Made sure to .lower so it changes everything to lowerscase 
# month = input("Please enter a month :").lower()
# # If statement that reads the month entered and prints out the correct amount of days for that month
# if month == "january" :
#     print("31 days")
# elif month == "february" :
#     print("28 or 29 days")
# elif month == "march" :
#     print("31 days")
# elif month == "april" :
#     print("30 days")
# elif month == "may" :
#     print("31 days")
# elif month == "june" :
#     print("30 days")
# elif month == "july" :
#     print("31 days")
# elif month == "august" :
#     print("31 days")
# elif month == "september" :
#     print("30 days")
# elif month == "october" :
#     print("31 days")
# elif month == "november" :
#     print("30 days")
# elif month == "december" :
#     print("31 days")
# else :
#     print("Please enter valid month")

# # Exercise 39
# # Creating user input for decibels
# num = int(input("Enter a number of decibels :"))
# # If statement to determine decibel range
# if num == 130 :
#     print("Thats a Jackhammer")
# elif num == 106 :
#     print("Thats a Gas lawnmower")
# elif num == 70 :
#     print("Thats an Alarm clock")
# elif num == 40 :
#     print("Thats a Quiet room")
# elif num < 40 :
#     print("Thats Quieter than a Quiet room")
# elif num > 130 :
#     print("Thats Louder than a Jackhammer")
#     # This is how to do in between numbers
# elif 70 < num < 106 :
#     print("Thats between an Alarm clock and a Gas lawnmower")
# elif 40 < num < 70 :
#     print("Thats between a Quiet room and an Alarm clock")
# elif 106 < num < 130 :
#     print("Thats between a Gas lawnmower and a Jackhammer")
# else :
#     print("Please enter a number")

# # Exercise 40
# side1 = float(input("Enter the length of side 1 :"))
# side2 = float(input("Enter the length of side 2 :"))
# side3 = float(input("Enter the length of side 3 :"))
# # if statement to determine if the sides are equal to each other
# if side1 == side2 == side3 :
#     print("This is an equilateral triangle")
# # if statement to determine if the sides are equal to each other
# elif side1 != side2 != side3 != side1 :
#     print("This is a scalene triangle")
# # if statement to determine if the sides are equal to each other
# else :
#     print("This is an isosceles triangle")

# # Exercise 43 
# # User input for money
# money = float(input("Enter a bill :"))
# # if statement to determine who the person is
# if money == 1 :
#     print("George Washington")
# elif money == 2 :
#     print("Thomas Jefferson")
# elif money == 5 :
#     print("Abraham Lincoln")
# elif money == 10 :
#     print("Alexander Hamilton")
# elif money == 20 :
#     print("Andrew Jackson")
# elif money == 50 :
#     print("Ulysses S. Grant")
# elif money == 100 :
#     print("Benjamin Franklin")
# else :
#     print("Please enter a valid amount")

# # Exercise 44
# # User input for month and day
# month = input("Enter a month :").lower()
# day = int(input("Enter a day :"))
# # if statement to determine holiday
# if month == "january" :
#     if day == 1 :
#         print("New Year's Day")
# if month == "july" :
#     if day == 1 :
#         print("Canada Day")
# if month == "december" :
#     if day == 25 :
#         print("Christmas Day")
# else : 
#     print("Does not correspond to a holiday")

# # Exercise 45
# def get_square_color(position):
#  # Extract the column letter and row number from the input
#     column_letter = position[0].lower()
#     row_number = int(position[1])
#  # Convert the column letter to a number 
#     column_number = ord(column_letter) - ord('a') + 1
#  # Determine if the sum of the column and row numbers is even or odd
#     if (column_number + row_number) % 2 == 0:
#         return "black"
#     else:
#         return "white"
# # Read the position from the user
# user_input = input("Enter the chessboard position : ")
# # Get the color of the square
# square_color = get_square_color(user_input)
# # print dinal
# print(f"The square {user_input} is {square_color}.")

# # Exercise 46
# def determine_season(month, day):
#     if (month == 'March' and day >= 20) or (month in ['April', 'May']) or (month == 'June' and day <= 20):
#         return 'Spring'
#     elif (month == 'June' and day >= 21) or (month in ['July', 'August']) or (month == 'September' and day <= 21):
#         return 'Summer'
#     elif (month == 'September' and day >= 22) or (month in ['October', 'November']) or (month == 'December' and day <= 20):
#         return 'Fall'
#     else:
#         return 'Winter'
# # Ask the user for the month and day
# month = input("Enter the name of the month : ")
# day = int(input("Enter the day of the month : "))
# # Figure out the season
# season = determine_season(month, day)
# # Show the result
# print("The date " + str(month) + " " + str(day) + " falls in the " + str(season) + " season.")

# # Exercise 47 
# # Define a function to determine the zodiac sign
# def get_zodiac_sign(month, day):
#     if (month == "december" and day >= 22) or (month == "january" and day <= 19):
#         return "capricorn"
#     elif (month == "january" and day >= 20) or (month == "february" and day <= 18):
#         return "aquarius"
#     elif (month == "february" and day >= 19) or (month == "march" and day <= 20):
#         return "pisces"
#     elif (month == "march" and day >= 21) or (month == 'april' and day <= 19):
#         return "aries"
#     elif (month == 'april' and day >= 20) or (month == "may" and day <= 20):
#         return "taurus"
#     elif (month == "may" and day >= 21) or (month == "June" and day <= 20):
#         return "gemini"
#     elif (month == "june" and day >= 21) or (month == "july" and day <= 22):
#         return "cancer"
#     elif (month == "july" and day >= 23) or (month == "august" and day <= 22):
#         return "leo"
#     elif (month == "august" and day >= 23) or (month == "september" and day <= 22):
#         return "virgo"
#     elif (month == "september" and day >= 23) or (month == "october" and day <= 22):
#         return "libra"
#     elif (month == "october" and day >= 23) or (month == "november" and day <= 21):
#         return "scorpio"
#     elif (month == "november" and day >= 22) or (month == "december" and day <= 21):
#         return "sagittarius"
# # Ask the user for their birth month and day
# month = input("Enter the name of your birth month: ")
# day = int(input("Enter the day of the month you were born : "))
# # Determine the zodiac sign
# zodiac_sign = get_zodiac_sign(month, day)
# # Display the result
# print("Your zodiac sign is " + str(zodiac_sign) + ".")

# # Exercise 48
# def get_chinese_zodiac(year):
#     chinese_zodiac = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
#     return chinese_zodiac[(year - 4) % 12]
# # User input for year
# year = int(input("Enter a year : "))
# # Determine the chinese zodiac year
# chinese_zodiac_year = get_chinese_zodiac(year)
# # Display the result
# print(f"The chinese zodiac year for {year} is {chinese_zodiac_year}.")

# # Exercise 49
# # User input for magnitude
# magnitude = float(input("Enter the magnitude of the earthquake : "))
# # if statement to determine magnitude
# if magnitude < 2 :
#     print("Micro")
# elif 2 <= magnitude < 3 :
#     print("Very minor")
# elif 3 <= magnitude < 4 :
#     print("Minor")
# elif 4 <= magnitude < 5 :
#     print("Light")
# elif 5 <= magnitude < 6 :
#     print("Moderate")
# elif 6 <= magnitude < 7 :
#     print("Strong")
# elif 7 <= magnitude < 8 :
#     print("Major")
# elif 8 <= magnitude < 10 :
#     print("Great")
# else :
#     print("Meterotic")

# # Exercise 50 
# # User input for values 
# a = float(input("Please enter value : "))
# b = float(input("Please enter value :"))
# c = float(input("Please enter value :"))
# # calculate the discrimnate 
# discriminant = b**2 - 4*a*c
# # if statement to determine roots
# if discriminant > 0 :
#     root1 = (-b + discriminant**0.5) / (2*a)
#     root2 = (-b - discriminant**0.5) / (2*a)
#     print("The roots are", root1, "and", root2)
# elif discriminant == 0 :
#     root = -b / (2*a)
#     print("The root is", root)
# else :
#     print("The equation has no real roots")

