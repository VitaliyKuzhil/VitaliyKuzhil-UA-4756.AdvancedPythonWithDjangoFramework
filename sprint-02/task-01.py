
def twoSidesOfWord(word:str) -> tuple:

    '''
    The function split up word on two equal peases

    Input:
    word

    Output:
    two peases of word
    '''

    middle = len(word) // 2

    return word[:middle], word[middle:]


def double_string(data:list) -> int:

    '''
    The function counts how many words in the list could be formed
    by concatenating or multiplying any existing words from the same list.
    It work only on that way when we can separate word on two equal peases.

    Input:
    list of words

    Output:
    number of words
    '''

    counter = 0

    for word in data:

        left, right = twoSidesOfWord(word)

        if data.count(left) >= 1 and data.count(right) >= 1:
            counter += 1

    return counter


# data = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
# print(double_string(data))

# data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qwerqwert']
# print(double_string(data))

# data = ['aa', 'abc', 'qwerqwer']
# print(double_string(data))

data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qweraaaa']
print(double_string(data))