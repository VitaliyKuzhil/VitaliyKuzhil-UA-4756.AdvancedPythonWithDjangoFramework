from cmath import sqrt

def solve_quadric_equation(a, b, c):
    
    try:
        a = float(a)
        b = float(b)
        c = float(c)

        if a == 0:
            raise ZeroDivisionError

        d = complex(b**2 - 4 * a * c)

        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
    
    except ZeroDivisionError:
        return 'Zero Division Error'
    except ValueError:
        return 'Could not convert string to float'
    
    else:
        return f'The solution are x1={x1} and x2={x2}'

    
print(solve_quadric_equation(1, 5, 6))