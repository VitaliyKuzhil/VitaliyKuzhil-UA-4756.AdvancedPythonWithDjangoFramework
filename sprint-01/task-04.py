
def findPermutation(p,q):

    # generated dictionary by element and it position into old list (p)
    elements_position = {p[i]: i+1 for i in range(len(p))}

    # generated new list according to following list (q)
    r = [elements_position[j] for j in q]

    # return final list
    return r


# p = [5, 1, 3]
# q = [3, 1, 5]

# current lists for permutation
p = [3, 4, 1, 2, 5]
q = [4, 5, 2, 3, 1]

print(findPermutation(p,q))
