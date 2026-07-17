
def calc(a, b, op):
    '''
    Function which define some operation:
    0: +
    1: -
    2: *
    3: /

    Return result of current operation:
    int|float (It depend on operation).
    
    Probably, some error is created and raised, such as:
    - ZeroDivisionError when second argument is zero;
    - TypeError when some of the operators aren't input correctly;
    - ValueError with information text weather incorrect operation come by.
    '''

    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    elif op == 3:
        return a / b

    raise ValueError('Incorrect operation is obtained')


def run_calc(a, b, op):
    '''
    Function which tried an execute calc function
    and share (a:digit, b: digit, op:operation) arguments to it.

    In occasion when in that function (calc) will create and rise an exception,
    this function will find a related handler for accrued exception.

    On another situation, when everything if fine this function will print a result.

    In both ways this function will show an ended massage of a program. 
    '''

    try:
        result = calc(a, b, op)
    
    except ZeroDivisionError as error:
        print('Division by zero')
    
    except TypeError:
        print('TypeError')
    
    except ValueError as error:
        print(error)
    
    else:
        print(result)
    
    finally:
        print('End of calculation')


run_calc(1, 2, 0)
run_calc(-19, "String", 3)
run_calc(42, 0, 3)