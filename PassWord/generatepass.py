import random
import string

LETTER = string.ascii_letters
NUMBER = string.digits
PUNCTATION = string.punctuation

printable = f"{LETTER}{NUMBER}{PUNCTATION}"

printable = list(printable)

random.shuffle(printable)

random_password = "".join(random.choices(printable, k=8))

print(random_password)
