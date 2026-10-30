def analyze_electricity_bills(monthly_units):
    bills = []
    for month, units in enumerate(monthly_units, start=1):
        fixed_charge = 50.0
        if units <= 100:
            bill = fixed_charge + (units * 3.0)
        elif units <= 300:
            bill = fixed_charge + (100 * 3.0) + ((units - 100) * 5.0)
        else:
            bill = fixed_charge + (100 * 3.0) + (200 * 5.0) + ((units - 300) * 8.0)
        bills.append((month, units, bill))

    print("--- Case Study 2: Electricity Bill Comparison ---")
    for i in range(len(bills)):
        m, u, b = bills[i]
        print(f"Month {m}: {u} units -> ${b:.2f}")
        if i > 0:
            prev_b = bills[i - 1][2]
            increase = b - prev_b
            if increase > 50:  # Threshold for unusual increase
                print(f"  ⚠️ Unusual increase detected! Jumped by ${increase:.2f}")


# Example Usage
analyze_electricity_bills([90, 150, 320, 480])