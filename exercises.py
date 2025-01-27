# 61 - 70 Darlin
"""
# Exercise 61:Average
# average = total/count of all numbers

total = 0
count = 0

while True:
    
    number = int(input("Enter number (0 to quit): "))
    total += number
    print(total)

    if(number == 0):
        break
    
    count += 1
    print(count)
    
average = total/count
print("your average is:", average)

# Exercise 62:Discount Table
# table = $4.95, $9.95, $14.95, $19.95, $24.95.

table = [4.95, 9.95, 14.95, 19.95, 24.95]
discount = 0.6
for i in range(len(table)):
    # i = index, so you cant multiply it 
    # print(f"${table[i]}", "discounted", f"${table[i*discount]}")
    original_price = table[i]
    discounted_price = original_price * discount
    print(f"${original_price} is discounted to ${discounted_price:.2f}")

# Exercise 63:Temperature ConversionTable

# 0 to 100 Celsius and Fahrenheit
# multiple of 10
# 1 celsius = 33.8 fahrenheit and vise versa

def Celsius_to_fahrenheit(c):
    return (c * 1.8) + 32

celsius = 0
for i in range(0, 101, 10):
    celsius = i
    fahrenheit = Celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")


# Exercise 64:No More Pennies

total_cost = 0
while True:
    price = input("Enter a price (press Enter to stop): ")
    
    if price == "":
        break
    
    if("$" in price):
        price = price.replace("$", "")
    
    price = float(price)
    total_cost += price
    
total_pennies = round(total_cost * 100) 
remainder = total_pennies % 5

if remainder < 2.5:
    cash_payment = (total_pennies - remainder) / 100  
else:
    cash_payment = (total_pennies + (5 - remainder)) / 100 

print(f"Total cost: ${total_cost:.2f}")
print(f"Cash payment: ${cash_payment:.2f}")
   

# Exercise 65:Compute the Perimeter of a Polygon
import math

polygon_points = []
perimeter = 0
while True:
    users_x = input("Enter the x part of the coordinate (blank to quit): ")
    users_y = input("Enter the y part of the coordinate: ")

    if (users_x == ""):
        break
    if (users_y == ""):
        break
    
    x = float(users_x)
    y = float(users_y)
    
    polygon_points.append((x, y))

if(len(polygon_points) > 1):
    for i in range(len(polygon_points) - 1):
        
        x1, y1 = polygon_points[i]
        x2, y2 = polygon_points[i + 1]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        perimeter += distance

x1, y1 = polygon_points[-1]
x2, y2 = polygon_points[0]
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
perimeter += distance
print(f"Perimeter: {perimeter:.2f}")

# Exercise 66:Compute a Grade Point Average (GPA)

grade_points = {
    "A+": 4.0, "A": 4.0, "A-": 3.7,
    "B+": 3.3, "B": 3.0, "B-": 2.7,
    "C+": 2.3, "C": 2.0, "C-": 1.7,
    "D+": 1.3, "D": 1.0, "F": 0.0
}

total_points = 0
num_grades = 0

while True:
    grade = input("Enter a letter grade (blank to quit): ").strip()
    if grade == "":
        break
    total_points += grade_points[grade.upper()]
    num_grades += 1

if num_grades > 0:
    gpa = total_points / num_grades
    print(f"The grade point average is {gpa:.1f}")
else:
    print("No grades were entered.")
 

# Exercise 67:Admission Price

total_cost = 0

while True:
    age_input = input("Enter the age of the guest (blank to quit): ").strip()
    if age_input == "":
        break
    
    age = int(age_input)

    if age <= 2:
        cost = 0.0
    elif 3 <= age <= 12:
        cost = 14.00
    elif age >= 65:
        cost = 18.00
    else:
        cost = 23.00

    total_cost += cost

print(f"The total admission cost for the group is ${total_cost:.2f}")


# Exercise 68:Parity Bits

while True:
    
    bit_string = input("Enter 8 bits (or press Enter to quit): ").strip()

    if bit_string == "":
        break
    # only 0's and 1's are allowed
    if len(bit_string) != 8 or any(char not in "01" for char in bit_string):
        print("Oops! Please enter exactly 8 bits (only 0s and 1s).")
        continue

    ones_count = bit_string.count("1")

    if ones_count % 2 == 0:
        parity_bit = 0
    else:
        parity_bit = 1

    # Tell the user what the parity bit should be
    print(f"Your input: {bit_string}")
    print(f"Parity bit: {parity_bit}")


# Exercise 69:Approximate π

pi_approximation = 3 
sign = 1
terms = 15

print("Approximations of π:")
for i in range(1, terms + 1):
    numerator = 4
    denominator = (2 * i) * (2 * i + 1) * (2 * i + 2)
    next_term = sign * (numerator / denominator)

    pi_approximation += next_term

    # Display the current approximation
    print(f"Approximation {i}: {pi_approximation:.15f}")

    # Alternate the sign for the next term
    sign *= -1
    
# Exercise 70:Caesar Cipher
def caesar_cipher(message, shift):
    # Resulting encoded/decoded message
    result = ""

    # Adjust the shift value to be within 0–25
    shift = shift % 26

    # Process each character in the message
    for char in message:
        # Check if it's an uppercase letter
        if char.isupper():
            new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            result += new_char
        # Check if it's a lowercase letter
        elif char.islower():
            new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            result += new_char
        else:
            # Non-letter characters are added as is
            result += char

    return result


# Get input from the user
message = input("Enter the message: ")
shift = int(input("Enter the shift value (positive for encoding, negative for decoding): "))

# Encode or decode the message
shifted_message = caesar_cipher(message, shift)

# Display the result
print("The shifted message is:")
print(shifted_message)
"""
