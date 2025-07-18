def calc_total(qty, price):
    total = qty * price
    if total > 10000:
        total = total * 0.9  # 10% discount
    return total

grand_total = 0
again = input("Do you want to do the program? (Yes or No): ")
while again.lower() == "yes":
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    total = calc_total(qty, price)
    print("Quantity:", qty)
    print("Price:", price)
    print("Total after discount (if any):", total)
    grand_total += total
    again = input("Do you want to do the program? (Yes or No): ")
print("Extended total of all purchases:", grand_total)

# Input: Quantity (float), Price (float)
# Process:
#   - Compute total = quantity * price
#   - If total > 10000.00, apply 10% discount
#   - Return discounted total
# Output:
#   - Display quantity, price, total (discounted if needed)
#   - Sum and display all totals at the end