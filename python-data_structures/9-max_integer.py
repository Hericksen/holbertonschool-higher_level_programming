def max_integer(my_list=[]):
    # Return None if the list is empty
    if len(my_list) == 0:
        return None

    # Initialize the maximum value with the first element of the list
    max_value = my_list[0]

    # Iterate through the list to find the maximum value
    for num in my_list:
        if num > max_value:
            max_value = num

    return max_value
