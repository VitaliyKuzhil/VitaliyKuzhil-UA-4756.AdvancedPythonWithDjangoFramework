
# responses
type_of_response = 'ascending', 'descending', 'not sorted'


# main function
def order(a):

    # current collection sorted by ascending
    sorted_collection = sorted(a)

    # compare current collection with sorted
    if a == sorted_collection:
        return type_of_response[0]
    
    # compare current collection with reflected
    elif a == sorted_collection[::-1]:
        return type_of_response[1]
    
    # not sorted type of collection
    else:
        return type_of_response[2]


# test collections
# a = [10, 5, 4] # descending
# a = [6, 20, 160, 420] # ascending
a = [1, 7, 0, 4, 8, 1] # not sorted


print(order(a))
