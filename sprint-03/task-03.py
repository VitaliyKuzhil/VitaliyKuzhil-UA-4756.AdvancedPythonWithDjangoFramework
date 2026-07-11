import re

password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^a-zA-Z\d\s]).{6,}$'

# def create_account(user_name: str, password: str, secret_words: list):

#     if not re.fullmatch(password_pattern, password):
#         raise ValueError('ValueError')


#     def check(current_password:str, current_words:list):

#         length_secret_words = len(secret_words)

#         return current_password == password \
#             and len(current_words) == length_secret_words\
#             and sum(1 for i in range(length_secret_words) if current_words[i] not in secret_words) <= 1

#     return check


def create_account(user_name: str, password: str, secret_words: list):

    if not re.fullmatch(password_pattern, password):
        raise ValueError('ValueError')


    def check(current_password: str, current_words: list):
        if current_password != password or len(current_words) != len(secret_words):
            return False
            
        temp_secret = secret_words.copy()
        errors = 0
        
        for word in current_words:
            if word in temp_secret:
                temp_secret.remove(word)
            else:
                errors += 1
                
        return errors <= 1
    
    return check


# tom = create_account("Tom", "Qwerty1", ["1", "word"]) # raises Value error 

	
user2 = create_account("User2", "yu6r*Tt5", ["word1", "abc3", "list"])
print(user2("yu6r*Tt5",["word1", "zzzz", "z"]))


# If
tom = create_account("Tom", "Qwerty1_", ["1", "word"]) 
# then
# 
print(tom("Qwerty1_",  ["1", "word"])) # return True 

print(tom("Qwerty1_",  ["word"])) # return False due to different length of   ["1", "word"] and  ["word"]

print(tom("Qwerty1_",  ["word", "12"])) # return True

print(tom("Qwerty1!",  ["word", "1"])) # return False because "Qwerty1!" not equals to "Qwerty1_"