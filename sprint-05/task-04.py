class ToSmallNumberGroupError(Exception):
    pass


def check_number(number):

    if number < 10:
        raise ToSmallNumberGroupError('The number is too small.')

    return f'Number of your group {number} is valid'
    


def check_number_group(group):
    try:
        number_of_group = check_number(int(group))
    except ToSmallNumberGroupError:
        return 'We obtain error:Number of your group can\'t be less than 10 '
    except ValueError:
        return 'You entered incorrect data. Please try again.'
    else:
        return number_of_group