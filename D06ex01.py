#Program to write ten random numbers to a file
######################################################################
#import statements
from random import randint as rint
######################################################################
#Body
def write_ten_numbers_to_file():
    with open("numberFile.txt","w") as file_object:
        iterator = 0;
        while(iterator < 5):
            file_object.write(str(rint(0,10000))+"\n")
            iterator += 1
######################################################################
#main
def main():
    write_ten_numbers_to_file()
    print("5 numbers written to file")
if __name__ == '__main__':
    main()
