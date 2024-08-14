def count_sheep(sheep_list):
    if not all(isinstance(sheep, bool) for sheep in sheep_list):
        raise ValueError("List should only contain boolean values")
    return sum(sheep for sheep in sheep_list if sheep is not None)


sheep_array = [True, True, True, False, True, True, True, True, True, False, True, False, True, False, False, True, True, True, True, True, False, False, True, True]
print(count_sheep(sheep_array))  # Output: 17