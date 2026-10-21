# Travel Fare Calculator
FARE_RATE = 14

while True:
    name = input("Enter passenger name: ")

    if name.strip() != "":
        break
    else:
        print("invalid name please try again")

while True:
    distance = float(input("Enter distance (km): "))

    if 1 <= distance:
        break
    else:
        print("use a valid number")

while True:
    passengers = int(input("Enter number of passengers: "))

    if 0 <= passengers:
        break
    else:
        print("use a positive integer")

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))

# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number
