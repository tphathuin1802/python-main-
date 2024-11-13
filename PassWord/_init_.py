import random
import string

LETTER = string.ascii_letters
NUMBER = string.digits
PUNCTATION = string.punctuation


def generate_password(length=8):
    printable = f"{LETTER}{NUMBER}{PUNCTATION}"
    printable = list(printable)
    random.shuffle(printable)
    random_password = random.choices(printable, k=length)
    random_password = "".join(random_password)
    return random_password


def input_length():
    password_length = input("Enter length of password: ").strip()
    return int(password_length)


def main():
    password_length = input_length()
    password = generate_password()
    print(password)

if __name__ == "__main__":
    main()
