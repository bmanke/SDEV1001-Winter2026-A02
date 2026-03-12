package = input("Enter the package: ")
hours_input = input("Enter the number of hours used: ")

try:
    hours = int(hours_input)
except ValueError:
    print("Please enter a valid number of hours")
    hours = 0

if package.upper() == 'A':
    if hours <= 10:
        total = 9.95
    else:
        total = 9.95 + (hours - 10) * 2.00
elif package.upper() == 'B':
    if hours <= 20:
        total = 13.95
    else:
        total = 13.95 + (hours - 20) * 1.00
elif package.upper() == 'C':
    total = 19.95

print(f"The total price is ${total}")