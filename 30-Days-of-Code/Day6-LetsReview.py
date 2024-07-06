# itertools is used for splitting odd and even indexes. 
# you can omit/join some lines to shorten the code

import itertools

t = int(input())
for i in range(1, (t+1)):
    word = input()
    letter_list = word.split()
    letter_list[:] = word

    even_i = itertools.islice(letter_list, 1, None, 2)
    odd_i = itertools.islice(letter_list, 0, None, 2)

    odd_list = list(odd_i)
    even_list = list(even_i)

    odd_word = ''.join(odd_list)
    even_word = ''.join(even_list)

    print(odd_word + " " + even_word)
