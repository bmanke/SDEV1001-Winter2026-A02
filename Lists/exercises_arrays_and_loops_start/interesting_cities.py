interesting_cities = ["Edmonton", "Paris", "Munich", "Berlin", "Amsterdam", "Prague"]

interesting_cities.remove("Edmonton")

interesting_cities.append(input("Enter a city that interests you: "))

interesting_cities.sort()

print("Our list of interesting cities in alphabetical order is:")
print(interesting_cities)