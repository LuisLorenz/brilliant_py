
my_str = 'This is a secret message that I want to keep private.' # global var

# str = my_str
# secure_str = str.replace('a', '|')
# secure_str = str.replace('g', 'a')
# secure_str = str.replace('|', 'g')

# print(secure_str) # This is a secret message that I want to keep private.
    # not working

#      str.replace('e', '|')
#     str.replace('f', 'e')
#     str.replace('|', 'f')'

# # 1) Exchaning simply one vocal type 
# changed_my_str = my_str.replace('e', '˘')

# print(changed_my_str) # This is a s˘cr˘t m˘ssag˘ that I want to k˘˘p privat˘.


# 2) Exchanging all the vocals
    # therefore create a func to avoid repetition of code 

# changed_my_str = None 
# def encrypting_str(my_str, old_char, new_char): 
#     changed_my_str = my_str.replace(old_char, new_char) # local var 
#     return changed_my_str # the str is returned 

# changed_my_str = encrypting_str(my_str, 'a', '#')
# changed_my_str = encrypting_str(my_str, 'e', '*') # the returned value is stored in my global var 

# print(changed_my_str) # This is a s*cr*t m*ssag* that I want to k**p privat*.
#     # only 'e' is exchanged
#     # because everytime the func is called it reverse to the original str and updates on specific char before returning it 
#     # solution: I have to upadet arg 'str' that serves as the base for the func 

# # changed_my_str = None 
# def encrypting_str(str, old_char, new_char): 
#     changed_str = str.replace(old_char, new_char) # local var 
#     return changed_str # the str is returned 

# # str = encrypting_str(str, 'a', '#') # the var can not be its arg!
# changed_str = encrypting_str(my_str, 'a', '#')
# changed_str_v2 = encrypting_str(changed_str, 'e', '*')

# print(changed_str_v2) # This is # s*cr*t m*ss#g* th#t I w#nt to k**p priv#t*.
#     # it worked but is not an efficient code!

# self.init
    # init always the code when self is called ...?


# 3) more efficient code
    # using a loop 
    # list of exchanging char: [('a', '#'), ('e', '*'), ('i', '_')]
    # for loop that inerates through that list: for i in list(): 
        # changed_str = str.replace(old_char, new_char) # local var 
        # return changed_str

# list
# char_list = [('a', '#'), ('e', '*'), ('i', '_')]
old_char = ['a', 'e', 'i']
new_char = ['#', '*', '_']

# # loop
# for i in old_char:
#     for x in new_char: 
#         changed_str = my_str.replace(i, x) # local var 

# print(changed_str) # Th_s _s a secret message that I want to keep pr_vate.  
#     # same problem: the original str is called and always return first to this base 
#     # solution: ...    

# for i in old_char:
#     for x in new_char: 
#         my_str = my_str.replace(i, x) # local var 

# print(my_str) # Th#s #s # s#cr#t m#ss#g# th#t I w#nt to k##p pr#v#t#.
#     # intersting 
#     # all the called vocals are replaced with '#' > why is that the case? 
#         # i = a
#             # x = # 
#             # ... *
#             # ... _ 
#         # i = e
#             # x = # 
#             # ... *
#             # ... _ 
#         # i = i 
#             # x = # 
#             # ... *
#             # ... _ 
#         # > makes sense: the vocal is only replaced once and then the char is not avaible in the str anymore 

# looping through both lists simulaneousely 

## zip func
# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica", "Vicky")

# x = zip(a, b)

# print(tuple(x)) # (('John', 'Jenny'), ('Charles', 'Christy'), ('Mike', 'Monica'))

# combi_list = zip(old_char, new_char)
# for x, y in combi_list:
#     my_str = my_str.replace(x, y)

# print(my_str) # Th_s _s # s*cr*t m*ss#g* th#t I w#nt to k**p pr_v#t*.
    # success! 

# efficient
    # I can simply change the combi list for making encryption stronger 


# 4) func for efficient encryption 

# combi_list = zip(old_char, new_char)

# def encryption(str):
#     for x, y in combi_list:
#         str = str.replace(x, y)
#     return str 

# encrypted_str = encryption(my_str)

# print(encrypted_str) # Th_s _s # s*cr*t m*ss#g* th#t I w#nt to k**p pr_v#t*.


# 5) Update Combi_list 
    # by adding tuples afterwards ideally (best overview)

# std_list = ['A', 'B']
# std_list.append('C')
# print(std_list)

# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica", "Vicky")

# x = zip(a, b)

# # here I have to convert the zip into an own list for using the append func 
# x = list(zip(a, b))
# x.append(('A', 'B'))

# print(x)

a = ['a', 'e', 'i']
b = ['#', '*', '_']
char_list = list(zip(a, b))

def encryption(str):
    for x, y in char_list:
        str = str.replace(x, y)
    return str 

# char = input('Input the char that should be encrypted: ')
# encryped_char = input(f'Input the encryption for the char {char}: ')

# char_list.append((char, encryped_char))

encrypted_str = encryption(my_str)

print(encrypted_str)
print(encryption(my_str))



