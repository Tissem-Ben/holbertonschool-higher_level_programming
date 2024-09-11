def element_at(my_list, idx):
    # Check if the index is within the valid range
    if idx < 0 or idx >= len(my_list):
        return None  # Return None if index is negative or out of range
    return my_list[idx]  # Return the element at the given index
