def get_pay(code, hours):
    if code.upper() == "L":
        rate = 25
    elif code.upper() == "A":
        rate = 30
    elif code.upper() == "J":
        rate = 50
    else:
        rate = 0
    if hours > 40:
        gross = 40 * rate + (hours - 40) * rate * 1.5
    else:
        gross = hours * rate
    return rate, gross

total_pay = 0
again = input("Do you want to do the program? (Yes or No): ")
while again.lower() == "yes":
    name = input("Enter employee last name: ")
    code = input("Enter job code (L, A, J): ")
    hours = float(input("Enter hours worked: "))
    rate, gross = get_pay(code, hours)
    print("Employee:", name)
    print("Hours Worked:", hours)
    print("Pay Rate: $", rate)
    print("Gross Pay: $", round(gross, 2))
    total_pay += gross
    again = input("Do you want to do the program? (Yes or No): ")
print("Total gross pay for all employees: $", round(total_pay, 2))

# Input: Last name (str), Job code (str), Hours worked (float)
# Process:
#   - Determine pay rate based on job code: L=$25, A=$30, J=$50
#   - Compute gross pay; overtime (over 40 hrs) is time and a half
#   - Return rate and gross pay
# Output:
#   - Display name, hours, rate, gross pay
#   - Display total gross pay for all employees
