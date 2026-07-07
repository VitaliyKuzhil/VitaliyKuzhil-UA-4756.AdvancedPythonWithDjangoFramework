def studying_hours(a):
    if not a:
        return 0
        
    max_len = 1
    current_len = 1
    
    for i in range(1, len(a)):
        if a[i] >= a[i-1]:
            current_len += 1
        else:
            current_len = 1
            
        if current_len > max_len:
            max_len = current_len
            
    return max_len


print(studying_hours([2, 2, 1, 3, 4, 1]))
