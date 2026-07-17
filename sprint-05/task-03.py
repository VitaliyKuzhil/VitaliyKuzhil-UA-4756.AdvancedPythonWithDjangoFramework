
weekdays = dict(zip(range(1,8), ('Monday', 'Tuesday', 'Wednesday', 
                                 'Thursday', 'Friday', 'Saturday', 'Sunday')))


def day_of_week(day):
    '''
    Function which try to change type of the data and after that find a value by key.

    When it couldn't change type of data raise ValueError
    When it couldn't find key into dictionary raise KeyError

    Finally, if datatype is integer and key exist into dictionary the result is returned
    '''
    try:
        result = weekdays[int(day)]
    except KeyError:
        return 'There is no such day of the week! Please try again.'
    except ValueError:
        return 'You did not enter a number! Please try again.'
    else:
        return result


print(day_of_week(5))
print(day_of_week('Sunday'))
print(day_of_week('Sun45'))
print(day_of_week('3'))
print(day_of_week(9))
