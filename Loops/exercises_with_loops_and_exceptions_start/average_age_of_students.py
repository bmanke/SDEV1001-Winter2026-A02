total_age = 0
count = 0

print("Average age of students calculator")
while True:
    user_input = input("Enter the age of a student or 'stop' to finish: ")
    
    if user_input.lower() == 'stop':
        break
    try:
        age = int(user_input)
        total_age += age
        count += 1
    except ValueError:
        print("Please enter a valid age or 'stop' to finish.")

if count == 0:
    print("You didn't enter any ages to average")
else:
    average = total_age / count
    print(f"The average age of the students is: {average}")