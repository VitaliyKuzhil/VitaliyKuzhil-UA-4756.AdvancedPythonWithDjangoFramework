def is_magic_square(matrix):
    n = len(matrix)
    if n == 0:
        return False
        
    # Collect all digits from matrix to collection
    all_numbers = []
    for row in matrix:
        for num in row:
            all_numbers.append(num)
            
    # Check unique and range from 1 to n^2
    required_numbers = set(range(1, n**2 + 1))
    if set(all_numbers) != required_numbers or len(all_numbers) != n**2:
        return False
        
    # Count magic constant
    magic_sum = sum(matrix[0])
    
    # Check sum all raws
    for row in matrix:
        if sum(row) != magic_sum:
            return False
            
    # Check sum all columns
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += matrix[i][j]
        if col_sum != magic_sum:
            return False
            
    # Check all diagonals
    diag1_sum = 0
    diag2_sum = 0
    for i in range(n):
        diag1_sum += matrix[i][i]        # main diagonal
        diag2_sum += matrix[i][n - 1 - i]  # side diagonal
        
    if diag1_sum != magic_sum or diag2_sum != magic_sum:
        return False
        
    return True


example_matrix = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]]


print(is_magic_square(example_matrix))
