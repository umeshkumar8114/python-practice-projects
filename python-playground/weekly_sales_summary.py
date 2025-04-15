# Tracks daily sales, validates input, and calculates summary statistics
sales = []
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for day in days:
    while True:
        try:
            amount = float(input(f"Enter sales for {day}: "))
            if amount < 0:
                raise ValueError
            sales.append(amount)
            break
        except ValueError:
            print("Invalid. Must be a non-negative number.")

print(f"Total: ${sum(sales):.2f}")
print(f"Max: ${max(sales):.2f}")
print(f"Min: ${min(sales):.2f}")