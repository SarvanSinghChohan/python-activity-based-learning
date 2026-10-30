def energy_conservation_analysis(appliances_usage):
    """
    appliances_usage: List of tuples -> (appliance_name, before_kwh, after_kwh)
    """
    results = []
    for name, before, after in appliances_usage:
        saved = before - after
        savings_pct = (saved / before) * 100 if before > 0 else 0
        results.append((name, saved, savings_pct))

    # Sort by percentage savings descending
    results.sort(key=lambda x: x[2], reverse=True)

    print("\n--- Case Study 68: Energy Conservation Analysis ---")
    for rank, (name, saved, pct) in enumerate(results, start=1):
        print(f"Rank {rank}: {name} | Saved: {saved} kWh ({pct:.1f}% reduction)")


# Example Usage
usage_data = [("AC Unit", 300, 240), ("Refrigerator", 150, 140), ("Lighting", 80, 50)]
energy_conservation_analysis(usage_data)