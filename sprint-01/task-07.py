# digits which contain visible zeros and points for them
score = {
    '0':1,
    '6':1,
    '9':1,
    '8':2
}

# calculate visible zeros into current number
def amountOfScoreFromNicky(number):
    return sum([score[i] for i in number if i in score])


# main function
def cipher_zeroes(N):

    # amount of points for visible zeros
    M = amountOfScoreFromNicky(N)

    # company law (requirements)
    if M % 2 == 0 and M > 0:
        M -= 1

    elif M % 2 != 0:
        M += 1
    
    # final result in binary numeral system
    return bin(M)[2:]

print(cipher_zeroes('565'))