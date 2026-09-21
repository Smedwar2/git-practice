def max_value(numbers):
    """This function returns the largest number
    in the list.
    """
    
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest