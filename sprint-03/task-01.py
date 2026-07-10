
def outer(name:str):

    '''
    Function outer get some <name> and return inner function.
    This inner function prints message "Hello, <name>!"

    Input outer function:
    name

    Output outer function:
    inner function

    Input inner function
    anything

    Output inner function
    massage
    '''

    def inner():
        print(f'Hello, {name}!')
    
    return inner


tom = outer("tom")

tom() # -> Hello, tom!
