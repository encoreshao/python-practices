# -*- coding: utf-8 -*-
#!/usr/bin/python3

# 这里是一个注释
# The second comment

'''
多行注释 1
多行注释 2
多行注释 3
'''

"""
多行注释 1
多行注释 2
多行注释 3
"""

print('Hello World!!!')

print("---------")

if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
    print ("False")

print("---------")

total = 1 + \
        2 + \
        3
print(total)

print("---------")

total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
print(total)

print("---------")

long_word = "This " "is " "Long " "string"
print(long_word)

print("---------")

str = 'Encore'
print(str)            # => Encore
print(str[0:-1])      # => Encor
print(str[0])         # => E
print(str * 2)        # => EncoreEncore
print(str + 'Shao')   # => Encore Shao
print(str[2:])        # => ncore
print('hello\nencore')
# hello
# Encore

# print(r'hello\nencore')   # => hello\nencore

print("---------")

input("\n\n按下 enter 键后退出。")

import sys; x = 'encore'; sys.stdout.write(x + '\n')

print('-------------')

x = "a"
y = "b"

print( x )
print( y )

print('-------------')

print( x, end=" "  )
print( y, end=" "  )
print()
