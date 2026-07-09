
def morse_number(number):
    
    result = ''
    step = 5

    for i in number:
        
        i = int(i)

        if 0 <= i <= 5:
            p = i
        else:
            p = i - 5

        current = ''
        
        for j in range(1, step+1): 
            if j <= p:
                current += '.' if i <= step else '-'
            else:
                current += '-' if i <= step else '.'
    
        result = ' '.join([result, current])
    
    return result.lstrip()

    # return ' '.join('.' * int(i) + '-' * (5 - int(i)) if int(i) <= 5 else '-' * (int(i) - 5) + '.' * (10 - int(i)) for i in number)

print(morse_number('2950'))