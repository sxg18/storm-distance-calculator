def calculate_distance(time_in_seconds):
    distance_in_miles = (time_in_seconds * 1100) / 5280
    distance_in_km = distance_in_miles * 1.60934
    return distance_in_km

# Example usage:
time_elapsed = float(input("Please enter the time elapsed after the lightning in seconds: "))
distance = calculate_distance(time_elapsed)
print("The distance of the lightning strike is", distance, "kilometers.")
