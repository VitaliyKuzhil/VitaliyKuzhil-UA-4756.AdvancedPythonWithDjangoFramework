
def isPalindrome(value):

    #get unique values from string
    unique_values = set(value)

    # counter for odd values
    odd_values = 0

    # iterating through unique collection
    for i in unique_values:

        # check if the character count is odd
        if value.count(i) % 2 != 0:

            # increase odd counter
            odd_values += 1

        # after each step check if we met odd more then one time
        if odd_values > 1:
            return False

    # return True if there is at most one odd-count character
    return True

print(isPalindrome(input()))



