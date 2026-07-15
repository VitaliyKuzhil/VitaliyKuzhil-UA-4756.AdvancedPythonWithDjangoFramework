
class Gallows:

    def __init__(self):
        self.words = list()
        self.game_over = False


    def play(self, word):
        if not self.game_over:

            # weather stack is empty
            if not self.words:
                self.words.append(word)
            # weather current word is'nt exist into stack
            elif word not in self.words:
                    # weather first character of current word match 
                    # to the last character of previous word
                    if self.words[-1][-1] == word[0]:

                        # add new relevant word into stack
                        self.words.append(word)
                    else:
                        # set game over
                        self.game_over = True  
                        return 'game over'
            else:
                # reset statement
                self.__init__()
                return 'game over'

        # return current words into stack
        return self.words


    def restart(self):

        # reset statement
        self.__init__()
        return 'game restarted'



my_gallows = Gallows()

print(my_gallows.play('apple')) # ➞ ['apple']
print(my_gallows.play('ear')) # ➞ ['apple', 'ear']
print(my_gallows.play('rhino')) # ➞ ['apple', 'ear', 'rhino']
print(my_gallows.words) # ➞ ['apple', 'ear', 'rhino']

# Words should be accessible.
print(my_gallows.restart()) # ➞ "game restarted"

# Words list should be set back to empty.
print(my_gallows.play('hostess')) # ➞ ['hostess']
print(my_gallows.play('stash') ) # ➞ ['hostess', 'stash']
print(my_gallows.play('hostess')) # ➞ "game over"

# Words cannot have already been said.
print(my_gallows.play('apple')) # ➞ ['apple']
print(my_gallows.play('ear')) # ➞ ['apple', 'ear']
print(my_gallows.play('rhino')) # ➞ ['apple', 'ear', 'rhino']
# Corn does not start with an "o".
print(my_gallows.play('corn')) # ➞ "game over"

print(my_gallows.words) # ➞ ['apple', 'ear', 'rhino']

print(my_gallows.restart()) # ➞ "game restarted"

print(my_gallows.words) # ➞ []
