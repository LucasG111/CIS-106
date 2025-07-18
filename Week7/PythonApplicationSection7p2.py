def get_batting_average(hits, at_bats):
    if at_bats == 0:
        return 0
    return hits / at_bats

count = 0
again = input("Do you want to do the program? (Yes or No): ")
while again.lower() == "yes":
    name = input("Enter last name: ")
    hits = int(input("Enter number of hits: "))
    at_bats = int(input("Enter number of at bats: "))
    avg = get_batting_average(hits, at_bats)
    print("Player:", name)
    print("Batting Average:", round(avg, 3))
    count += 1
    again = input("Do you want to do the program? (Yes or No): ")
print("Number of players entered:", count)

# Input: Last name (str), Hits (int), At-bats (int)
# Process:
#   - Compute batting average = hits / at-bats
#   - Return batting average
# Output:
#   - Display last name and batting average
#   - Display total count of players entered