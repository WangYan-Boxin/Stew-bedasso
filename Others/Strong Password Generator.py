import random

words = ["Andy", "Terry", "Alex", "Eric", "Max", "Mark"]
symbols = ["!", "@", "#", "$", "%", "&", "*"]

all_passwords = []

for i in range(5):
    word1 = random.choice(words)
    word2 = random.choice(words)
    symbol = random.choice(symbols)
    number = random.randint(10, 99)

    if number > 50:
        word1 = word1.capitalize()
    else:
        word2 = word2.capitalize()

    password_list = [word1, symbol, str(number), word2]

    random.shuffle(password_list)

    first_password = "".join(password_list)

    magic = list(first_password)
    random.shuffle(magic)

    second_password = "".join(magic)

    all_passwords.append(second_password)

print("".join(all_passwords))

