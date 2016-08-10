#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1:
#       2:
#       3:
##############################################################################
# Imports

# Body
def uses_only(word, string_of_letters):
    for each_letter in word:
        if(each_letter not in string_of_letters):
            return False
    return True

def sentence_generator():
    with open("words.txt","r") as file_object:
        for each_line in file_object:
            if(uses_only(each_line.strip(),"acefhlo")):
                print(each_line.strip())
    file_object.close()

##############################################################################
def main():
    sentence_generator()

if __name__ == '__main__':
    main()
