#!/usr/bin/python3
def remove_char_at(input_str, n):
    if n < 0 or n >= len(input_str):
        # If the index is out of bounds, return the original string
        return input_str
    
    # Create a copy of the string with the character at index n removed
    result_str = input_str[:n] + input_str[n+1:]
    
    return result_str
