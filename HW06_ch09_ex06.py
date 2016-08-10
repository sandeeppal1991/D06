#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write additional function(s) to assist you
#   - number of abecedarian words: 6
##############################################################################
# Imports

# Body
def is_abecedarian(word):
    converted_list_word = list(word)
    sorted_list_word = sorted(converted_list_word, reverse = False)
    if(converted_list_word == sorted_list_word):
        return True
    else:
        return False
def no_of_abecedarian_words():
    no_of_words = 0
    with open("words.txt","r") as file_object:
        for each_line in file_object:
            if(is_abecedarian(each_line.strip())):
                no_of_words += 1
    print('No of abecedarian words are : '+ str(no_of_words))
    file_object.close()
##############################################################################
def main():
    no_of_abecedarian_words()

if __name__ == '__main__':
    main()
