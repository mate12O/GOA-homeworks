def can_reach_pump(distance_to_pump, fuel_left, fuel_efficiency):
    # Calculate the maximum distance the car can travel with the remaining fuel
    max_distance = fuel_left * fuel_efficiency
    # Check if the maximum distance is greater than or equal to the distance to the pump
    return max_distance >= distance_to_pump


distance_to_pump = 50
fuel_left = 2
fuel_efficiency = 25

print(can_reach_pump(distance_to_pump, fuel_left, fuel_efficiency))  # Output: True