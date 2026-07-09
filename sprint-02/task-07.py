import re

pattern = r'0+[a-z]{4}$'

def pretty_message(data):
    return [i for i in re.split(r'\ |\.', data) if re.search(pattern, i)]


# data = "0msdfgh 00000xbcd 0bbcd7 hjkj00wjhg hjkj0ajhg"

data = "0Regular0 expressions0 provide0 a0 flexible0 and0 concise0 way0 to0 se0arch and0 manipu0late text0 data0 in0 str0ings."

print(pretty_message(data))