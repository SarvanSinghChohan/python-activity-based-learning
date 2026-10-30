def water_tariff_analysis(households_consumption):
    """
    households_consumption: List of tuples -> (household_id, liters_consumed)
    """
    print("\n--- Case Study 25: Progressive Water Tariff Analysis ---")
    threshold = 3000
    for hid, usage in households_consumption:
        bill = 20.0  # Fixed fee
        if usage <= 1000:
            bill += usage * 0.01
        elif usage <= 3000:
            bill += (1000 * 0.01) + ((usage - 1000) * 0.02)
        else:
            bill += (1000 * 0.01) + (2000 * 0.02) + ((usage - 3000) * 0.05)
            bill += 50.0  # Excessive usage penalty

        status = "Normal Usage"
        if usage > threshold:
            status = "🚨 Excessive Usage Warning"

        print(f"Household {hid}: {usage}L | Bill: ${bill:.2f} | Status: {status}")


# Example Usage
data_water = [("H101", 800), ("H102", 2500), ("H103", 4200)]
water_tariff_analysis(data_water)