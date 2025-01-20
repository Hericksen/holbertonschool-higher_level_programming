def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the original list if the index is invalid
    my_list[idx] = element  # Replace the element at the specified index
    return my_list
