import string
import random

str1 = string.ascii_letters
str2 = string.digits
str3 = string.punctuation
str = []
try:

    plen = input("Enter password length ")
    if not(plen.isdigit()):
        raise ValueError("Enter a number")


except ValueError as e:
    print(e)
    plen = input("Enter Password length: ")
finally:
    str.extend(list(str1))
    str.extend(list(str2))
    str.extend(list(str3))
    # random.shuffle(s)
    sample_list = random.sample(str, int(plen))
    print("Your password is: ")
    print("".join(sample_list[:int(plen)]))

