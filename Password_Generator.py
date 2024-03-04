import random

UPPER_CASES = "QWERTYUIOPASDFGHJKLZXCVBNM"
LOWER_CASES = "qwertyuiopasdfghjklzxcvbnm"
NUMBERS = "1234567890"
SPECIAL_CHARACTERS = "~!@#$%^&*)(|><"

ALL_CHARACTERS = UPPER_CASES + LOWER_CASES + NUMBERS + SPECIAL_CHARACTERS

def generate_password(length):
    code = []
    
    code.append(UPPER_CASES[random.randint(0,25)])
    code.append(LOWER_CASES[random.randint(0, 25)])
    code.append(NUMBERS[random.randint(0,9)])
    code.append(SPECIAL_CHARACTERS[random.randint(0, 12)])
    code.append(ALL_CHARACTERS[random.randint(0,71)])
    
    while len(code) < length:
        code.append(ALL_CHARACTERS[random.randint(0, 72)])
    code = "".join(code)
    feedback = "Your password is as follows"
    return feedback, code
       
print(generate_password(12))