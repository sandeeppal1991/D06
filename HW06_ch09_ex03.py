#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

# Body


def avoids(word_to_check, forbidden_letters):
    for each_letter in word_to_check:
        if each_letter in forbidden_letters:
            return False
    return True


def forbidden_prompt():
    try:
        forbidden_letters = input("Enter the forbidden string : ")
    except Exception as e:
        if(type(e).__name__ == "ValueError"):
            print("You must enter an integer !" )
        else:
            print("Please enter something ! ")
    with open("words.txt","r") as file_object:
        for each_line in file_object:
            if(avoids(each_line.strip(),forbidden_letters)):
                print(each_line.strip())
        file_object.close()
    print("No of words not forbidden : " + str(forbidden_param(forbidden_letters)))


def forbidden_param(forbidden_letters):
    count_of_not_forbidden_words = 0
    with open("words.txt","r") as file_object:
        for each_line in file_object:
            if(avoids(each_line.strip(),forbidden_letters)):
                count_of_not_forbidden_words += 1
        file_object.close()
    return count_of_not_forbidden_words

def find_five():
    list_of_alphabet_count = [0]*26
    with open("words.txt","r") as file_object:
        for each_line in file_object:
            for each_letter in each_line.strip():
                list_of_alphabet_count[ord(each_letter.lower())-ord('a')] += 1

    iterator = 0
    forbidden_letters = ""
    forbidden_indexes = sorted(range(len(list_of_alphabet_count)), key=lambda i: list_of_alphabet_count[i], reverse=True)[:5]
    while(iterator < 5):
        forbidden_letters += chr(forbidden_indexes[iterator]+ord('a'))
        iterator += 1
    print("A combination of 5 forbidden letters that excludes the smallest number of words : " + forbidden_letters )
    print("No of forbidden words in the list of words : "+ str(forbidden_param(forbidden_letters)))



##############################################################################
def main():
    ...
    # Your final submission should only call five_five
    forbidden_prompt()
    find_five()

if __name__ == '__main__':
    main()
