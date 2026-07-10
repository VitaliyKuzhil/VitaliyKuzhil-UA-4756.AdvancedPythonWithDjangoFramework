
def create(origin_string:str):

    '''
    Function create one string argument and return anonymous function that checks 
    if the argument of function is equals to the argument of outer function.

    Input outer function:
    origin_string

    Output outer function:
    anonymous function

    Input anonymous function:
    compare_string

    Output anonymous function
    True|False
    '''

    return lambda compare_string: origin_string == compare_string


tom = create("pass_for_Tom")

print(tom("pass_for_Tom")) # returns true 

print(tom("pass_for_tom")) # returns false