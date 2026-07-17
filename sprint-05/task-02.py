import re


def check_email(string):
    '''
    Function which received a string and compare it with email_pattern
    by using Regular Expression. Current function create and raise an
    exception ValueError with text weather string isn't match with
    email_pattern (re.match return None).

    Otherwise this function return True
    '''
    email_pattern = r'(^\w+)@{1}([a-z]+)\.?([a-z]+)?\.([a-z]+$)'

    if re.match(email_pattern, string) is None:
        raise ValueError('Email isn\'t valid')

    return True


def valid_email(string):
    '''
    Function which tried an execute check_email function and pass a string to it.

    When into check_email raise ValueError exception this function will try handle
    accrued exception and return a massage 'Email is not valid'.

    When check_email return True it's mean that email is valid and handle exception
    block will not start instead block else returned a massage 'Email is valid'
    '''
    try:
        check_email(string)
    except ValueError:
        return 'Email is not valid'
    else:
        return 'Email is valid'
