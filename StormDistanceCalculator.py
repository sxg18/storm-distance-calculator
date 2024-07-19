def calculate_distance(time_in_seconds):
    distance_in_miles = round((time_in_seconds * 1100) / 5280, 2)
    distance_in_km = round(distance_in_miles * 1.60934, 2)
    return distance_in_miles, distance_in_km

# Example usage:
time_elapsed = float(input("Please enter the time elapsed after the lightning in seconds: "))
distance_in_miles, distance_in_km = calculate_distance(time_elapsed)
print("The distance of the lightning strike is", distance_in_miles, "miles (or", distance_in_km, "kilometers).")
