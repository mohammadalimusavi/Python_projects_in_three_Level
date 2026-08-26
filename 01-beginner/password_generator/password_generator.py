import random

words_box = ['a', 'b', 'c' 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

len_of_password = int(input('Enter the length of the password to generate: '))

result = random.sample(words_box, len_of_password)

print(f"This your password: {"".join(result)}")

