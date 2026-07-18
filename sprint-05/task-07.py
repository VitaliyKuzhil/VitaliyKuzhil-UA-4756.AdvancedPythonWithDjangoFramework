class MyExceptions(Exception):
    '''
    The exception raise when:
    - if non-numbers or numbers less than 1 were entered;
    - if non-numbers obtained from array;
    - if when one of the numbers or both is larger than the array length.
    '''
    pass


def check_positive_numbers(*args):
    for i in args:
        if i < 1:
            raise MyExceptions
    return True


def sum_slice_array(arr, first = 1, second = 1):

    try:
        number1, number2 = int(first), int(second)

        check_positive_numbers(number1, number2)

        result = float(int(arr[number1-1]) + int(arr[number2-1]))
    
    except (IndexError, ValueError):
        raise MyExceptions

    else:
        return result


	
try:
    print(sum_slice_array([14, 5, 3], 1, 5))
except MyExceptions:
    print("MyExceptions")