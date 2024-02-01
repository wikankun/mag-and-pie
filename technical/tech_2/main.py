def smallest_less_five(number):
    # initialize the variables
    digit_to_remove = '5'
    min_number = None
    number_length = len(number)
    is_negative = number[0] == ('-')

    # check if it's a negative number with only one digit number
    if is_negative and number_length == 2:
        if int(number) == -5:
            return 0
        else:
            return int(number)
        
    # check if it's not a negative number with only one digit number
    if not is_negative and number_length == 1:
        if int(number) == 5:
            return 0
        else:
            return int(number)

    # iterate to find the best digit_to_remove to remove
    for i, digit in enumerate(number):
        if digit == digit_to_remove:
            # if minimum number combination is None
            # or the new combination without current digit is lower than minimum number combination
            # then save the current digit
            if min_number is None or int(number[:i] + number[i+1:]) < min_number:
                min_number = int(number[:i] + number[i+1:])

    return min_number