
my_str = 'This is a secret message that I want to keep private.'

str = my_str
secure_str = str.replace('a', '|')
secure_str = str.replace('g', 'a')
secure_str = str.replace('|', 'g')

print(secure_str) # This is a secret message that I want to keep private.
    # not working

#      str.replace('e', '|')
#     str.replace('f', 'e')
#     str.replace('|', 'f')'