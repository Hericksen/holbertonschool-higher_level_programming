#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if idx is valid (within the range of the list)
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the list unchanged if idx is invalid

    # Create a new list excluding the element at the specified index
    new_list = my_list[:idx] + my_list[idx+1:]

    return new_list
