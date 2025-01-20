#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Create a new list to store the results
    result = []

    # Iterate through the original list
    for num in my_list:
        # Check if the number is divisible by 2 and append the result (True/False)
        result.append(num % 2 == 0)

    return result
