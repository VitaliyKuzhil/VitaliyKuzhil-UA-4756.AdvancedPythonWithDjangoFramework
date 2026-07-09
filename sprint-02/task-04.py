import re

pattern = r'(\w{1,3}?)\1+'

def pretty_message(string):
    return re.sub(pattern, r'\1', string, count=0, flags=re.IGNORECASE)


data = "Thisssssssss isisisis echooooooo stringggg. Replaceaceaceace repeatedededed groupssss of symbolssss"
print(pretty_message(data))

# data = "Another input data string"
# print(pretty_message(data))