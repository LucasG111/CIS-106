def trip_info(miles, gallons):
    mpg = miles / gallons if gallons != 0 else 0
    cost = gallons * 3.00
    return mpg, cost

trip_count = 0
total_miles = 0
total_cost = 0
again = input("Do you want to do the program? (Yes or No): ")
while again.lower() == "yes":
    city = input("Enter destination city: ")
    miles = float(input("Enter miles traveled: "))
    gallons = float(input("Enter gallons used: "))
    mpg, cost = trip_info(miles, gallons)
    print("City:", city)
    print("Miles:", miles)
    print("Miles Per Gallon:", round(mpg, 2))
    print("Gas Cost: $", round(cost, 2))
    trip_count += 1
    total_miles += miles
    total_cost += cost
    again = input("Do you want to do the program? (Yes or No): ")
print("Number of trips:", trip_count)
print("Total miles traveled:", total_miles)
print("Total gas cost: $", round(total_cost, 2))

# Input: Destination city (str), Miles traveled (float), Gallons used (float)
# Process:
#   - Compute mpg = miles / gallons
#   - Compute gas cost = gallons * 3.00
#   - Return mpg and gas cost
# Output:
#   - Display destination, miles, mpg, gas cost
#   - Display total trips, total miles, total gas cost