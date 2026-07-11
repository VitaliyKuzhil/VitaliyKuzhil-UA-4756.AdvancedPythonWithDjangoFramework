def logger(func):
    def wraper(*args:tuple, **kwargs:dict):
        
        result = func(*args, **kwargs)
        
        all_arguments = list(args) + list(kwargs.values())
        
        formed_string = ", ".join(map(str, all_arguments))
        
        print(f'Executing of function {func.__name__} with arguments {formed_string}...')
        
        return result
    
    return wraper

@logger
def sum(a,b):
    return a+b
    
@logger
def print_arg(arg):
    print(arg)
    
@logger
def concat(*args:tuple, **kwargs:dict):
    all_arguments = list(args) + list(kwargs.values())
    return ''.join(map(str, all_arguments))


print(concat('first string', second = 2, third = 'second string'))

print_arg(2)

dict_args={'first kwarg' :0, 'second kwarg': 'second kwarg'}
concat(**dict_args)