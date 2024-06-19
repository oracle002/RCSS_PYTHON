# 1.2. Program to calculate electricity bill based on consumption

def calculate_electricity_bill(units):
    if units <= 200:
        bill = units * 0.50
    elif units <= 400:
        bill = 200 * 0.50 + (units - 200) * 0.65
    elif units <= 600:
        bill = 200 * 0.50 + 200 * 0.65 + (units - 400) * 0.80
    else:
        bill = 200 * 0.50 + 200 * 0.65 + 200 * 0.80 + (units - 600) * 1.00
    
    if bill > 400:
        surcharge = bill * 0.15
        bill += surcharge
    
    if bill < 100:
        bill = 100
    
    return bill

# Test the electricity bill calculation
units_consumed = int(input("Enter Units "))
electricity_bill = calculate_electricity_bill(units_consumed)
print(f"Electricity bill for {units_consumed} units: Rs. {electricity_bill:.2f}")