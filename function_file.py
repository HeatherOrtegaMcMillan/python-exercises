# my function file

def string_money_to_float(string):
    """
    this function takes in a string with a dollar sign and commas and returns a float ready for math
    
    """
    char_to_replace = {'$': '',
                    ',': ''}
    # Iterate over all key-value pairs in dictionary
    for key, value in char_to_replace.items():
        # Replace key character with value character in string
        string = string.replace(key, value)
    return float(string)
