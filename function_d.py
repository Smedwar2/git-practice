def max_value(numbers):
    """This function returns the largest number
    in the list.
    """
    print(max_value([3,2,8,9,4,6)]))
    
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest