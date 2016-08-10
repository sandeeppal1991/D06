#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body
def has_no_e(word):
    if(word.strip().find('e') == -1):
        return True
    else:
        return False


def print_no_e():
    file_object = open("words.txt")
    total_no_of_words = 0
    no_of_words_without_e = 0
    for word in file_object:
        total_no_of_words += 1
        if(has_no_e(word)):
            no_of_words_without_e += 1
            print(word.strip())
    print("Percentage of words without the character 'e' is " + str((no_of_words_without_e*100) / total_no_of_words)+"%")
    file_object.close()
##############################################################################
def main():
    print_no_e()

if __name__ == '__main__':
    main()
