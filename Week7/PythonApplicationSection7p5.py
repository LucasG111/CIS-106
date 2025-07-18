def tuition(credits, district):
    if district.upper() == "I":
        return credits * 250
    else:
        return credits * 550

total_tuition = 0
again = input("Do you want to do the program? (Yes or No): ")
while again.lower() == "yes":
    name = input("Enter student last name: ")
    credits = int(input("Enter credit hours: "))
    code = input("Enter district code (I or O): ")
    owed = tuition(credits, code)
    print("Student:", name)
    print("Tuition Owed: $", round(owed, 2))
    total_tuition += owed
    again = input("Do you want to do the program? (Yes or No): ")
print("Total tuition owed by all students: $", round(total_tuition, 2))

# Input: Last name (str), Credit hours (int), District code (str)
# Process:
#   - Determine cost per credit: I=$250, O=$550
#   - Compute tuition = hours * cost per credit
#   - Return tuition
# Output:
#   - Display name and tuition
#   - Display total tuition for all students