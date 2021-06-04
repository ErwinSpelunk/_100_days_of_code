# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:40:58 2021

1/100 days of code

@author: Erwin
"""

print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")

# using ', " to be used if nested
# escape may be used by \"
print("print('this')")
print('print("this")')
print('print(\'this\')')

# Multiline string, but tabs spaces etc get translated, too
fake_variable = '_'
print("""Hello world!
      Hello Again!\n
Cruel World!""")

print(f"""Hello world!
      Hello Again!\n
Cruel World!""")

# use a backslash \ to join multiline strings
print('Hello World!\n' \
      "Hello Again!\n" \
          f'Cruel World!{fake_variable}')
    
print('\nNEXT:\n')
print("Day 1 - String Manipulation")
print("String Concatenation is done with the \"+\" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n. Namely \\n.")

print('\nNEXT 1-09:\n')    

print("Hello " + input("What is your name?") + "!")

print('\nNEXT 1-10:\n')    

print(len(input('What is your name?')))

print('\nNEXT 1-12:\n')    


# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a
a = b
b = c

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

print('\nNEXT 1-MAIN:\n')
print('Welcome to the band name generator!')
pet = input('What was your childhood pet?\n')
place = input('In which city were you born?\n')
print(f'A cool band name would be {place} {pet}!\nRock On!')