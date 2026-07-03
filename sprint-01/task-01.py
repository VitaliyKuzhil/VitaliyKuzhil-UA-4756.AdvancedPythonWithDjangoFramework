# Constraints
# ----------------------------------------------------------------------------
def checkBase(base):
    return 2 <= base <= 30


def checkExponent(exponent):
    return 1 <= exponent <= 100

# ----------------------------------------------------------------------------


# Get digits
# ----------------------------------------------------------------------------
def getBase():
    while True:
        base = int(input('Write a base (from 2 to 30): '))

        if checkBase(base):
            return base

        print('Incorrect value! Base must be between 2 and 30. Try again.')


def getExponent():
    while True:
        exponent = int(input('Write an exponent (from 1 to 100): '))

        if checkExponent(exponent):
            return exponent

        print('Incorrect value! Exponent must be between 1 and 100. Try again.')


n, k = getBase(), getExponent()
# ----------------------------------------------------------------------------


# Final function
# ----------------------------------------------------------------------------
def kthTerm(n, k):

    # Approach one
    # ------------------------------------------------------------------------

    # main_list = [n**0]

    # for i in range(1, k+1):
    #     current_base = n**i

    #     current_list = [current_base]

    #     for j in main_list:
    #         current_list.append(current_base+j)
        
    #     main_list.extend(current_list)
    
    # main_list.sort()

    # return main_list[k-1]
    # ------------------------------------------------------------------------


    # Approach two
    # ------------------------------------------------------------------------
    binary_number = [int(i) for i in reversed(bin(k)[2:])]

    result = 0
    for j in range(len(binary_number)):
        if binary_number[j] == 1:
            result += n**j
    
    return result
    # ------------------------------------------------------------------------

print(kthTerm(n,k))

# ----------------------------------------------------------------------------
