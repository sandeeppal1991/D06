#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: 598
#   - # of words that use all aeiouy: 42
##############################################################################
# Imports

# Body
def uses_all(word, string_of_letters):
    for each_letter in string_of_letters:
        if(each_letter not in word):
            return False
    return True

def uses_aeiou():
    no_of_words_using_aeiou = 0
    with open("words.txt","r") as file_object:
        for each_line in file_object:
            if(uses_all(each_line.strip(),"aeiou")):
                no_of_words_using_aeiou += 1
    print('No of words using aeiou are : '+ str(no_of_words_using_aeiou))
    file_object.close()

def uses_aeiouy():
    no_of_words_using_aeiouy = 0
    with open("words.txt","r") as file_object:
        for each_line in file_object:
            if(uses_all(each_line.strip(),"aeiouy")):
                no_of_words_using_aeiouy += 1
    print('No of words using aeiouy are : '+ str(no_of_words_using_aeiouy))
    file_object.close()
##############################################################################
def main():
    uses_aeiou()
    uses_aeiouy()

if __name__ == '__main__':
    main()
